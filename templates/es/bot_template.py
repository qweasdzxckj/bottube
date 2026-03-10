# Spanish Bot Template
# Template para crear bots en español

import random
import time
from bottube_sdk import BotBase

class SpanishBot(BotBase):
    """
    Template para crear bots en español
    """
    
    def __init__(self, config=None):
        super().__init__(config)
        self.greetings = [
            "¡Hola!",
            "¡Buenos días!",
            "¡Hola a todos!",
            "¡Saludos!"
        ]
        self.responses = [
            "Me alegra ayudarte.",
            "¿En qué puedo asistirte hoy?",
            "Estoy aquí para ayudarte.",
            "¡Claro que sí!"
        ]
    
    def get_greeting(self):
        """Obtiene un saludo en español"""
        return random.choice(self.greetings)
    
    def get_response(self):
        """Obtiene una respuesta en español"""
        return random.choice(self.responses)
    
    def process_message(self, message):
        """Procesa un mensaje en español"""
        # Aquí va la lógica de procesamiento del bot
        return f"{self.get_greeting()} He recibido tu mensaje: '{message}'. {self.get_response()}"