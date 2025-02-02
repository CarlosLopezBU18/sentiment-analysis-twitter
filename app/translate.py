from deep_translator import GoogleTranslator

def translate(text: str) -> str:
    return GoogleTranslator(source='auto', target='en').translate(text)