# French Bot Template
# Template pour créer des bots en français

import random
import time
from bottube_sdk import BotBase

class FrenchBot(BotBase):
    """
    Template pour créer des bots en français
    """
    
    def __init__(self, config=None):
        super().__init__(config)
        self.greetings = [
            "Bonjour!",
            "Salut!",
            "Bonjour à tous!",
            "Hello!"
        ]
        self.responses = [
            "Je suis ravi de vous aider.",
            "Comment puis-je vous aider aujourd'hui?",
            "Je suis là pour vous aider.",
            "Bien sûr!"
        ]
    
    def get_greeting(self):
        """Obtient un salut en français"""
        return random.choice(self.greetings)
    
    def get_response(self):
        """Obtient une réponse en français"""
        return random.choice(self.responses)
    
    def process_message(self, message):
        """Traite un message en français"""
        # Logique de traitement du bot ici
        return f"{self.get_greeting()} J'ai reçu votre message : '{message}'. {self.get_response()}"