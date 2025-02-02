from asyncio import run
import threading as th
from googletrans import Translator

class GTranslator:
    
    _trans = Translator()

    async def _translate(text: str):
        detection = await GTranslator._trans.detect(text=text)
        
        if detection.lang == 'en':
            return text, True
        
        translation = await GTranslator._trans.translate(text=text)
        return translation.pronunciation, False
    
    def translate(text: str):
        return run(GTranslator._translate(text=text))