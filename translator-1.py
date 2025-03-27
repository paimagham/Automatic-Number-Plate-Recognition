import googletrans
import pyttsx3

def translate_and_speak(text, source_language='hi', target_language='ko'):
  """
  Translates text from Hindi to Korean and reads the translated text aloud in English.

  Args:
      text: The text to be translated.
      source_language: The source language code (e.g., 'en' for English, 'hi' for Hindi).
      target_language: The target language code (e.g., 'ko' for Korean).
  """

  translator = googletrans.Translator()
  try:
    translation = translator.translate(text, src=source_language, dest=target_language)
    korean_text = translation.text

    # Text-to-speech setup (adjust voice and rate as needed)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Change index for different voices (0 for default)
    engine.setProperty('rate', 150)  # Adjust speaking rate (default is 200)

    engine.say(korean_text)
    engine.runAndWait()

  except Exception as e:
    print(f"Translation failed: {e}")

# Example usage:
text_to_translate = "नमस्ते"  # Hindi for "Hello"

translate_and_speak(text_to_translate)
