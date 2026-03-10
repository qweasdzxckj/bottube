# Bot Language Comments
# This file contains language-specific comments and utilities for multilingual bots

# Language codes
LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    'zh-CN': 'Chinese (Simplified)',
    'fr': 'French',
    'de': 'German',
    'ja': 'Japanese',
    'ko': 'Korean',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'ar': 'Arabic'
}

# Common bot phrases in different languages
BOT_PHRASES = {
    'greeting': {
        'en': 'Hello!',
        'es': '¡Hola!',
        'zh-CN': '你好！',
        'fr': 'Bonjour!',
        'de': 'Hallo!',
        'ja': 'こんにちは！',
        'ko': '안녕하세요!',
        'pt': 'Olá!',
        'ru': 'Привет!',
        'ar': 'مرحبا!'
    },
    'help': {
        'en': 'How can I help you?',
        'es': '¿Cómo puedo ayudarte?',
        'zh-CN': '我能帮你做什么？',
        'fr': 'Comment puis-je vous aider?',
        'de': 'Wie kann ich Ihnen helfen?',
        'ja': 'どのようにお手伝いできますか？',
        'ko': '어떻게 도와드릴까요?',
        'pt': 'Como posso ajudar você?',
        'ru': 'Как я могу вам помочь?',
        'ar': 'كيف يمكنني مساعدتك؟'
    },
    'goodbye': {
        'en': 'Goodbye!',
        'es': '¡Adiós!',
        'zh-CN': '再见！',
        'fr': 'Au revoir!',
        'de': 'Auf Wiedersehen!',
        'ja': 'さようなら！',
        'ko': '안녕히 가세요!',
        'pt': 'Tchau!',
        'ru': 'До свидания!',
        'ar': 'وداعا!'
    }
}

def get_phrase(phrase_type, language='en'):
    """Get a phrase in the specified language"""
    return BOT_PHRASES.get(phrase_type, {}).get(language, BOT_PHRASES.get(phrase_type, {}).get('en', ''))

def get_supported_languages():
    """Get list of supported languages"""
    return list(LANGUAGES.keys())

def is_language_supported(language):
    """Check if a language is supported"""
    return language in LANGUAGES