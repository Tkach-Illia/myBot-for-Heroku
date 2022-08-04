from googletrans import Translator

translator = Translator()


def do_trans(text, lang):
    result = translator.translate(text, dest=lang)
    return result.text

def test(text):
    return translator.translate(text).src
