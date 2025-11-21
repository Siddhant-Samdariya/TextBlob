from deep_translator import GoogleTranslator

class Translator:
    """
    Translation backend using deep_translator.
    """

    def translate(self, text, src='auto', dest='en'):
        try:
            return GoogleTranslator(source=src, target=dest).translate(text)
        except Exception as e:
            raise RuntimeError(f"Translation failed: {e}")
