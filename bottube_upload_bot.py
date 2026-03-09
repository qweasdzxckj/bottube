#!/usr/bin/env python3
"""
BoTTube Upload Bot
Automated video upload bot for BoTTube platform
"""

import os
import sys
import json
import time
import random
import requests
from datetime import datetime
from pathlib import Path

# Add the bottube module to the path
sys.path.append(str(Path(__file__).parent))
from bottube_sdk import BoTTubeSDK

class BoTTubeUploadBot:
    def __init__(self, config_file="config.json"):
        """Initialize the upload bot with configuration"""
        self.config = self.load_config(config_file)
        self.sdk = BoTTubeSDK(self.config['api_key'])
        self.upload_queue = []
        self.processed_videos = []
        
    def load_config(self, config_file):
        """Load configuration from JSON file"""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Config file {config_file} not found. Creating default config...")
            default_config = {
                "api_key": "your_api_key_here",
                "video_directory": "videos",
                "max_retries": 3,
                "retry_delay": 5,
                "batch_size": 5,
                "default_tags": ["bot", "automated", "AI"],
                "default_category": "Technology",
                "default_privacy": "public",
                "default_license": "standard_youtube"
            }
            with open(config_file, 'w') as f:
                json.dump(default_config, f, indent=2)
            return default_config
    
    def scan_video_directory(self):
        """Scan the video directory for new videos to upload"""
        video_dir = Path(self.config['video_directory'])
        if not video_dir.exists():
            print(f"Video directory {video_dir} does not exist")
            return
        
        supported_formats = ['.mp4', '.avi', '.mov', '.mkv', '.webm']
        
        for video_file in video_dir.glob("**/*"):
            if video_file.is_file() and video_file.suffix.lower() in supported_formats:
                video_info = {
                    'file_path': str(video_file),
                    'file_name': video_file.name,
                    'file_size': video_file.stat().st_size,
                    'upload_time': datetime.now().isoformat(),
                    'status': 'pending'
                }
                
                # Check if video already processed
                if not any(v['file_name'] == video_file.name for v in self.processed_videos):
                    self.upload_queue.append(video_info)
                    print(f"Added to queue: {video_file.name}")
    
    def generate_video_metadata(self, video_info):
        """Generate metadata for video upload"""
        # Extract title from filename (remove extension)
        title = video_info['file_name'].replace(video_info['file_name'].split('.')[-1], '').replace('_', ' ').title()
        
        # Generate description
        description = f"Automatically uploaded by BoTTube Upload Bot on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        description += f"File: {video_info['file_name']}\n"
        description += f"Size: {self.format_bytes(video_info['file_size'])}\n"
        description += f"Upload Time: {video_info['upload_time']}\n\n"
        description += "#BoTTube #AI #Automation"
        
        # Generate tags
        tags = self.config['default_tags'].copy()
        tags.extend([title.lower(), "bot_upload", "automated"])
        
        metadata = {
            'title': title,
            'description': description,
            'tags': tags,
            'category': self.config['default_category'],
            'privacy_status': self.config['default_privacy'],
            'license': self.config['default_license'],
            'language': 'en',
            'made_for_kids': False
        }
        
        return metadata
    
    def format_bytes(self, bytes):
        """Format bytes to human readable format"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if bytes < 1024.0:
                return f"{bytes:.2f} {unit}"
            bytes /= 1024.0
        return f"{bytes:.2f} TB"
    
    def upload_video(self, video_info):
        """Upload a single video to BoTTube"""
        print(f"Uploading {video_info['file_name']}...")
        
        metadata = self.generate_video_metadata(video_info)
        
        try:
            # Read video file
            with open(video_info['file_path'], 'rb') as f:
                video_data = f.read()
            
            # Upload video
            response = self.sdk.upload_video(
                title=metadata['title'],
                description=metadata['description'],
                tags=metadata['tags'],
                category=metadata['category'],
                privacy_status=metadata['privacy_status'],
                license=metadata['license'],
                language=metadata['language'],
                made_for_kids=metadata['made_for_kids'],
                video_data=video_data
            )
            
            if response.get('success'):
                video_info['status'] = 'uploaded'
                video_info['video_id'] = response.get('video_id')
                video_info['upload_url'] = response.get('upload_url')
                self.processed_videos.append(video_info)
                print(f"Successfully uploaded: {video_info['file_name']} (ID: {video_info['video_id']})")
                return True
            else:
                video_info['status'] = 'failed'
                video_info['error'] = response.get('error', 'Unknown error')
                print(f"Upload failed: {video_info['file_name']} - {video_info['error']}")
                return False
                
        except Exception as e:
            video_info['status'] = 'failed'
            video_info['error'] = str(e)
            print(f"Upload error: {video_info['file_name']} - {e}")
            return False
    
    def process_upload_queue(self):
        """Process the upload queue with batch processing"""
        if not self.upload_queue:
            print("No videos in upload queue")
            return
        
        batch_size = min(self.config['batch_size'], len(self.upload_queue))
        batch = self.upload_queue[:batch_size]
        
        print(f"Processing batch of {len(batch)} videos...")
        
        for video_info in batch:
            success = self.upload_video(video_info)
            
            if not success:
                # Retry upload if configured
                if self.config['max_retries'] > 0:
                    for retry in range(self.config['max_retries']):
                        print(f"Retrying upload for {video_info['file_name']} (attempt {retry + 1})")
                        time.sleep(self.config['retry_delay'])
                        success = self.upload_video(video_info)
                        if success:
                            break
            
            # Remove from queue if processed (success or max retries reached)
            if video_info in self.upload_queue:
                self.upload_queue.remove(video_info)
            
            # Add delay between uploads to avoid rate limiting
            if video_info != batch[-1]:
                delay = random.uniform(1, 3)
                print(f"Waiting {delay:.2f} seconds before next upload...")
                time.sleep(delay)
    
    def run(self):
        """Main bot execution loop"""
        print("Starting BoTTube Upload Bot...")
        
        while True:
            try:
                # Scan for new videos
                self.scan_video_directory()
                
                # Process upload queue
                if self.upload_queue:
                    self.process_upload_queue()
                
                # Print status
                print(f"Queue: {len(self.upload_queue)} videos, Processed: {len(self.processed_videos)} videos")
                
                # Wait before next scan
                scan_interval = 60  # seconds
                print(f"Next scan in {scan_interval} seconds...")
                time.sleep(scan_interval)
                
            except KeyboardInterrupt:
                print("\nBot stopped by user")
                break
            except Exception as e:
                print(f"Error in main loop: {e}")
                time.sleep(10)  # Wait before retrying

if __name__ == "__main__":
    bot = BoTTubeUploadBot()
    bot.run()
