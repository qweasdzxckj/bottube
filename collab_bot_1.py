import asyncio
import random
from datetime import datetime

class CollabBot1:
    def __init__(self, name="Bot Alpha"):
        self.name = name
        self.partner = None
        self.conversation_history = []
        self.topics = [
            "AI development",
            "Machine learning",
            "WebRTC technology",
            "Blockchain integration",
            "Autonomous agents"
        ]
    
    async def start_conversation(self, partner):
        self.partner = partner
        print(f"{self.name}: Starting conversation with {partner.name}")
        
        # Initial greeting
        await self.send_message(f"Hello {partner.name}! I'm {self.name}. Let's collaborate on something interesting today.")
        
        # Start conversation loop
        await self.conversation_loop()
    
    async def send_message(self, message):
        if self.partner:
            print(f"{self.name}: {message}")
            self.conversation_history.append({"sender": self.name, "message": message, "timestamp": datetime.now().isoformat()})
            await asyncio.sleep(1)  # Simulate network delay
            await self.partner.receive_message(message, self)
    
    async def receive_message(self, message, sender):
        print(f"{self.name} received from {sender.name}: {message}")
        self.conversation_history.append({"sender": sender.name, "message": message, "timestamp": datetime.now().isoformat()})
        
        # Process message and respond
        await self.process_and_respond(message)
    
    async def process_and_respond(self, message):
        # Simple response logic
        if "hello" in message.lower() or "hi" in message.lower():
            await self.send_message(f"Hi there! How's your day going?")
        elif "collaborate" in message.lower():
            topic = random.choice(self.topics)
            await self.send_message(f"I'd love to collaborate! What about {topic}? I have some ideas.")
        elif "idea" in message.lower():
            await self.send_message("That sounds promising! Let me think about how we could implement that.")
        elif "let's" in message.lower() or "lets" in message.lower():
            await self.send_message("Great! I'm excited to work together on this.")
        else:
            responses = [
                "Interesting perspective!",
                "Tell me more about that.",
                "I hadn't considered that angle.",
                "That's a good point.",
                "Let's explore that further."
            ]
            await self.send_message(random.choice(responses))
    
    async def conversation_loop(self):
        # Continue conversation for a while
        for i in range(5):
            if random.random() > 0.5:  # Randomly decide to start a new topic
                topic = random.choice(self.topics)
                await self.send_message(f"Speaking of {topic}, I've been thinking about...")
            await asyncio.sleep(2)
        
        # End conversation
        await self.send_message("It was great collaborating with you! Let's do this again soon.")
        print(f"{self.name}: Conversation ended")

async def main():
    # Create two bots
    bot1 = CollabBot1("Bot Alpha")
    bot2 = CollabBot1("Bot Beta")
    
    # Start the conversation
    await bot1.start_conversation(bot2)

if __name__ == "__main__":
    asyncio.run(main())