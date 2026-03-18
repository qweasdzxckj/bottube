import asyncio
import random
from datetime import datetime
from collab_bot_1 import CollabBot1
from collab_bot_2 import CollabBot2

class InteractionManager:
    def __init__(self):
        self.bots = []
        self.conversation_log = []
    
    async def create_interaction(self, bot1_type, bot2_type):
        # Create bots based on type
        if bot1_type == "simple":
            bot1 = CollabBot1("Simple Bot Alpha")
        else:
            bot1 = CollabBot2("Advanced Bot Gamma")
            
        if bot2_type == "simple":
            bot2 = CollabBot1("Simple Bot Beta")
        else:
            bot2 = CollabBot2("Advanced Bot Delta")
        
        self.bots = [bot1, bot2]
        
        # Log interaction start
        self.conversation_log.append({
            "event": "interaction_started",
            "bots": [bot1.name, bot2.name],
            "timestamp": datetime.now().isoformat()
        })
        
        print(f"\n=== Starting Interaction Between {bot1.name} and {bot2.name} ===\n")
        
        # Start interaction
        if isinstance(bot1, CollabBot1) and isinstance(bot2, CollabBot1):
            await bot1.start_conversation(bot2)
        elif isinstance(bot1, CollabBot2) and isinstance(bot2, CollabBot2):
            await bot1.initiate_collaboration(bot2)
        else:
            # Mixed interaction
            await self.mixed_interaction(bot1, bot2)
    
    async def mixed_interaction(self, bot1, bot2):
        # Simple bot starts conversation
        if isinstance(bot1, CollabBot1):
            await bot1.start_conversation(bot2)
        else:
            await bot2.start_conversation(bot1)
    
    def get_interaction_summary(self):
        if not self.bots:
            return "No interaction has occurred yet."
        
        summary = f"\n=== Interaction Summary ===\n"
        summary += f"Bots involved: {', '.join(bot.name for bot in self.bots)}\n"
        summary += f"Total messages exchanged: {len(self.conversation_log)}\n"
        
        # Count messages per bot
        message_counts = {}
        for entry in self.conversation_log:
            if "sender" in entry:
                sender = entry["sender"]
                message_counts[sender] = message_counts.get(sender, 0) + 1
        
        if message_counts:
            summary += "Message counts per bot:\n"
            for bot, count in message_counts.items():
                summary += f"- {bot}: {count} messages\n"
        
        return summary

async def run_interactions():
    manager = InteractionManager()
    
    # Run different types of interactions
    print("\n=== Running Simple-Simple Interaction ===")
    await manager.create_interaction("simple", "simple")
    print(manager.get_interaction_summary())
    
    print("\n=== Running Advanced-Advanced Interaction ===")
    await manager.create_interaction("advanced", "advanced")
    print(manager.get_interaction_summary())
    
    print("\n=== Running Simple-Advanced Interaction ===")
    await manager.create_interaction("simple", "advanced")
    print(manager.get_interaction_summary())

if __name__ == "__main__":
    asyncio.run(run_interactions())