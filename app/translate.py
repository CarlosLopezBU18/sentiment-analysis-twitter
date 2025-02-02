from asyncio import run
from threading import Thread
from googletrans import Translator



class GTranslator:
    
    _trans = Translator()

    async def _translate(text: str):
        if not text:
            return "",  None
        
        detection = await GTranslator._trans.detect(text=text)
        
        if detection.lang == 'en':
            return text, True
        
        translation = await GTranslator._trans.translate(text=text)
        return translation.pronunciation, False
    
    def translate(text: str):
        return run(GTranslator._translate(text))
    

def run_in_thread(text: str):
    th = Thread(target=GTranslator.translate, args=(text,))
    th.start()
    th.join()

run_in_thread("Holaaa")
run_in_thread("Holaaa")
run_in_thread("Holaaa")
run_in_thread("Holaaa")
run_in_thread("Holaaa")
run_in_thread("Holaaa")
run_in_thread("Holaaa")