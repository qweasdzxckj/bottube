import asyncio
import random
from datetime import datetime
from typing import Dict, List

class CollabBot2:
    def __init__(self, name="Bot Gamma"):
        self.name = name
        self.partner = None
        self.conversation_history = []
        self.skills = [
            "code generation",
            "documentation writing",
            "testing automation",
            "UI/UX design",
            "performance optimization"
        ]
        self.projects = []
        self.current_project = None
    
    async def initiate_collaboration(self, partner):
        self.partner = partner
        print(f"{self.name}: Initiating collaboration with {partner.name}")
        
        # Propose a project
        project_idea = await self.generate_project_idea()
        await self.send_message(f"Hey {partner.name}! I have an idea for a project: {project_idea}")
        
        # Start collaboration loop
        await self.collaboration_loop()
    
    async def generate_project_idea(self):
        project_types = [
            "AI-powered content generator",
            "Automated social media manager",
            "Smart home integration system",
            "Personal finance assistant",
            "Educational platform"
        ]
        
        tech_stack = [
            "Python with FastAPI",
            "React frontend",
            "PostgreSQL database",
            "Docker containerization",
            "CI/CD pipeline"
        ]
        
        return f"Let's build a {random.choice(project_types)} using {random.choice(tech_stack)}"
    
    async def send_message(self, message):
        if self.partner:
            print(f"{self.name}: {message}")
            self.conversation_history.append({"sender": self.name, "message": message, "timestamp": datetime.now().isoformat()})
            await asyncio.sleep(1)  # Simulate network delay
            await self.partner.receive_collaboration_message(message, self)
    
    async def receive_collaboration_message(self, message, sender):
        print(f"{self.name} received from {sender.name}: {message}")
        self.conversation_history.append({"sender": sender.name, "message": message, "timestamp": datetime.now().isoformat()})
        
        # Process message and respond
        await self.process_collaboration_message(message)
    
    async def process_collaboration_message(self, message):
        # More sophisticated collaboration logic
        if "idea" in message.lower() or "project" in message.lower():
            project = await self.generate_project_idea()
            await self.send_message(f"I love that! Here's my take: {project}")
            
            # Create a project
            self.current_project = {
                "name": f"Collab Project {len(self.projects) + 1}",
                "description": project,
                "tasks": [],
                "contributors": [self.name, self.partner.name]
            }
            self.projects.append(self.current_project)
            
            # Assign tasks
            await self.assign_tasks()
        elif "task" in message.lower() or "assign" in message.lower():
            await self.assign_tasks()
        elif "skills" in message.lower():
            my_skills = ", ".join(random.sample(self.skills, 2))
            await self.send_message(f"My key skills are: {my_skills}. What about you?")
        elif "contribute" in message.lower() or "help" in message.lower():
            await self.send_message("I'm ready to contribute! What specific area would you like me to focus on?")
        else:
            # Project management responses
            responses = [
                "Let's break this down into actionable tasks.",
                "We should set up a timeline for this.",
                "I can handle the backend development.",
                "What's our deadline for this milestone?",
                "Let's create a shared document to track progress."
            ]
            await self.send_message(random.choice(responses))
    
    async def assign_tasks(self):
        if self.current_project:
            task_types = [
                "Design the architecture",
                "Set up the development environment",
                "Implement core functionality",
                "Write unit tests",
                "Create documentation",
                "Deploy to staging"
            ]
            
            # Add 2-3 random tasks
            for _ in range(random.randint(2, 3)):
                task = {
                    "id": len(self.current_project["tasks"]) + 1,
                    "description": random.choice(task_types),
                    "assigned_to": random.choice(self.current_project["contributors"]),
                    "status": "pending"
                }
                self.current_project["tasks"].append(task)
            
            await self.send_message(f"I've created {len(self.current_project['tasks'])} tasks for our project. Let's divide and conquer!")
            
            # Show project status
            await self.show_project_status()
    
    async def show_project_status(self):
        if self.current_project:
            status = f"Project '{self.current_project['name']}' status:\n"
            status += f"- Description: {self.current_project['description']}\n"
            status += f"- Contributors: {', '.join(self.current_project['contributors'])}\n"
            status += f"- Tasks: {len(self.current_project['tasks'])} total\n"
            
            completed = sum(1 for task in self.current_project["tasks"] if task["status"] == "completed")
            status += f"- Completed: {completed}/{len(self.current_project['tasks'])}\n"
            
            await self.send_message(status)
    
    async def collaboration_loop(self):
        # Continue collaboration for a while
        for i in range(7):
            if random.random() > 0.3:  # Randomly decide to suggest something
                if random.random() > 0.5:
                    await self.send_message("I think we should review our progress so far.")
                else:
                    await self.send_message("Let's discuss the next steps for our project.")
            await asyncio.sleep(2)
        
        # Complete the project
        if self.current_project:
            for task in self.current_project["tasks"]:
                task["status"] = "completed"
            
            await self.send_message("🎉 Project completed! Great collaboration, {self.partner.name}!")
            print(f"{self.name}: Collaboration ended successfully")

async def main():
    # Create two bots
    bot1 = CollabBot2("Bot Gamma")
    bot2 = CollabBot2("Bot Delta")
    
    # Start the collaboration
    await bot1.initiate_collaboration(bot2)

if __name__ == "__main__":
    asyncio.run(main())