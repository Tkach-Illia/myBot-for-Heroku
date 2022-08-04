from googletrans import Translator

translator = Translator()

def do_trans(text, lang):
    return translator.translate(text, dest=lang).text

def test(text):
    return translator.translate(text).src
