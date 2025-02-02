import pytest
from app.translate import GTranslator

def test_translate():
    translated_text, is_eng = GTranslator.translate(text="Hola que tal como estás")
    assert translated_text == "Hello, how are you"
    assert is_eng == False

    translated_text, is_eng = GTranslator.translate(text="Hello how are you")
    assert translated_text == "Hello how are you"
    assert is_eng == True

    translated_text, is_eng = GTranslator.translate(text="")
    assert translated_text == ""
    assert is_eng == None

    translated_text, is_eng = GTranslator.translate(text="¿Cómo estás? ¡Bien!")
    assert translated_text == "How are you? Good!"
    assert is_eng == False

def test_detect():
    _, detected_lang = GTranslator.translate(text="Hola que tal como estás")
    assert detected_lang == False

    _, detected_lang = GTranslator.translate(text="Hello how are you")
    assert detected_lang == True

    _, detected_lang = GTranslator.translate(text="")
    assert detected_lang == None

    _, detected_lang = GTranslator.translate(text="¿Cómo estás? ¡Bien!")
    assert detected_lang == False

def test_translate_error_handling():
    with pytest.raises(ValueError):
        GTranslator.translate(text=None)

    with pytest.raises(ValueError):
        GTranslator.translate(text=12345)

def test_detect_error_handling():
    with pytest.raises(ValueError):
        GTranslator.detect(text=None)

    with pytest.raises(ValueError):
        GTranslator.detect(text=12345)


def test_translate_multiple_languages():
    translated_text, is_eng = GTranslator.translate(text="Bonjour comment ça va")
    assert translated_text == "Hello how are you"
    assert is_eng == False

    translated_text, is_eng = GTranslator.translate(text="Hallo wie geht es dir")
    assert translated_text == "Hello how are you"
    assert is_eng == False

def test_translate_performance():
    import time
    start_time = time.time()
    GTranslator.translate(text="Hola que tal como estás")
    end_time = time.time()
    assert (end_time - start_time) < 1.0