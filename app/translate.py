from asyncio import run
from googletrans import Translator

class GTranslator:
    def __init__(self):
        self.trans = Translator()

    async def _detect(self, text: str):
        return await self.trans.detect(text=text)
    
    async def _api_call(self, text: str):
        return await self.trans.translate(text=text)
    
    def is_english(self, text: str):
        return run(self._detect(text=text)).lang == 'en'

    def translate(self, text: str):
        return run(self._api_call(text=text))