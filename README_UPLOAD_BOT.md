# BoTTube Upload Bot

## Overview

The BoTTube Upload Bot is an automated video upload tool designed to streamline the process of uploading videos to the BoTTube platform. It scans a specified directory for video files, generates appropriate metadata, and uploads them in batches while handling retries and error management.

## Features

- **Automatic Video Scanning**: Monitors a directory for new video files
- **Batch Processing**: Uploads videos in configurable batch sizes
- **Metadata Generation**: Automatically generates titles, descriptions, and tags
- **Retry Mechanism**: Configurable retry attempts for failed uploads
- **Error Handling**: Comprehensive error logging and management
- **Rate Limiting**: Built-in delays to avoid API rate limits

## Installation

1. Ensure you have Python 3.6+ installed
2. Install required dependencies:
   ```bash
   pip install requests
   ```
3. Place the `bottube_upload_bot.py` script in your project directory
4. Create a `videos` directory to store your video files

## Configuration

Create a `config.json` file with the following structure:

```json
{
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
```

### Configuration Options

- `api_key`: Your BoTTube API key
- `video_directory`: Directory to scan for video files
- `max_retries`: Maximum number of retry attempts for failed uploads
- `retry_delay`: Delay in seconds between retry attempts
- `batch_size`: Number of videos to process in each batch
- `default_tags`: Default tags to apply to all videos
- `default_category`: Default category for videos
- `default_privacy`: Privacy status (public, private, unlisted)
- `default_license`: License type for videos

## Usage

1. Update your `config.json` with your BoTTube API key
2. Place your video files in the specified video directory
3. Run the bot:
   ```bash
   python bottube_upload_bot.py
   ```
4. The bot will continuously scan the directory and upload videos

## Supported Video Formats

- MP4
- AVI
- MOV
- MKV
- WebM

## API Integration

The bot uses the BoTTube SDK for API integration. Make sure your API key has the necessary permissions for video uploads.

## Logging

The bot provides console output with detailed information about:
- Videos added to the queue
- Upload progress and status
- Errors and retry attempts
- Processing statistics

## Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your API key is valid and has upload permissions
2. **File Not Found**: Check that your video directory exists and contains video files
3. **Upload Failures**: Check your internet connection and API rate limits
4. **Permission Errors**: Ensure the bot has read access to video files

### Debug Mode

For detailed debugging, you can modify the script to add more verbose logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Contributing

To contribute to the BoTTube Upload Bot:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue in the BoTTube repository
- Contact the BoTTube development team

## Changelog

### Version 1.0.0
- Initial release
- Basic video upload functionality
- Batch processing
- Retry mechanism
- Configuration file support