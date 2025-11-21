from googletrans import Translator as GoogleTranslator

class Translator:
    def __init__(self):
        self.translator = GoogleTranslator()

    def translate(self, text, src='auto', dest='en'):
        try:
            result = self.translator.translate(text, src=src, dest=dest)
            return result.text
        except Exception as e:
            raise RuntimeError(f"Translation failed: {e}")
