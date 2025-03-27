from googletrans import Translator


def translate_text(text, source_lang, target_lang):
    """
  Translates text from source_lang to target_lang using Google Translate API.

  Args:
      text: The text to be translated.
      source_lang: The source language code (e.g., 'en' for English).
      target_lang: The target language code (e.g., 'es' for Spanish).

  Returns:
      The translated text.
  """
    translator = Translator()
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text


# Example usage
text_to_translate = "Hello My name is SaiBhavitha Reddy?"
source_language = 'en'  # English
target_language = 'ko'  # Spanish

translated_text: object = translate_text(text_to_translate, source_language, target_language)

print(f"Original Text: {text_to_translate}")
print(f"Translated Text ({target_language}): {translated_text}")
