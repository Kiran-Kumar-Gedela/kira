import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

def voice_to_translation():
    # List of supported languages and their codes
    language_codes = {
        'Supported Indian Languages': {
            'Bengali': 'bn',
            'Gujarati': 'gu',
            'Hindi': 'hi',
            'Kannada': 'kn',
            'Malayalam': 'ml',
            'Tamil': 'ta',
            'Telugu': 'te',
            'Urdu': 'ur',
        },
        'Supported International Languages': {
            'Arabic': 'ar',
            'Chinese (Simplified)': 'zh-CN',
            'Dutch': 'nl',
            'English': 'en',
            'French': 'fr',
            'German': 'de',
            'Italian': 'it',
            'Japanese': 'ja',
            'Korean': 'ko',
            'Portuguese': 'pt',
            'Russian': 'ru',
            'Spanish': 'es',
            'Turkish': 'tr',
            'Vietnamese': 'vi'
        }
    }

    # Display supported languages
    print("Supported Indian Languages:")
    for lang in sorted(language_codes['Supported Indian Languages']):
        print(lang)

    print("\nSupported International Languages:")
    for lang in sorted(language_codes['Supported International Languages']):
        print(lang)

    # Ask the user for the source and target languages
    source_choice = input("\nSelect the source language:\n1. Indian\n2. International\nChoose 1 or 2: ").strip()
    
    if source_choice == '1':
        source_lang = input("Enter the source language (name): ").strip()
        src_code = language_codes['Supported Indian Languages'].get(source_lang)
    elif source_choice == '2':
        source_lang = input("Enter the source language (name): ").strip()
        src_code = language_codes['Supported International Languages'].get(source_lang)
    else:
        print("Invalid choice for source language.")
        return

    if not src_code:
        print("Invalid language input. Please enter valid language names.")
        return

    target_choice = input("\nSelect the target language:\n1. Indian\n2. International\nChoose 1 or 2: ").strip()

    if target_choice == '1':
        target_lang = input("Enter the target language (name): ").strip()
        tgt_code = language_codes['Supported Indian Languages'].get(target_lang)
    elif target_choice == '2':
        target_lang = input("Enter the target language (name): ").strip()
        tgt_code = language_codes['Supported International Languages'].get(target_lang)
    else:
        print("Invalid choice for target language.")
        return

    if not tgt_code:
        print("Invalid language input. Please enter valid language names.")
        return

    # Use the microphone as the source
    with sr.Microphone() as source:
        print("Listening for your voice...")
        audio_data = recognizer.listen(source)
        print("Recognizing...")
        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data, language=src_code)
            print(f"You said: {text}")

            # Translate the text to the target language
            translated_text = GoogleTranslator(source=src_code, target=tgt_code).translate(text)
            print(f"Translated to {target_lang}: {translated_text}")

            # Speak the translated text
            test_tts(translated_text, tgt_code)

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

def test_tts(translated_text, language_code):
    try:
        # Test TTS engine with the translated text
        print("Speaking the translated text...")
        tts = gTTS(text=translated_text, lang=language_code)
        tts.save("translated.mp3")
        os.system("start translated.mp3")  # For Windows
        print("Done speaking.")

    except Exception as e:
        print(f"An error occurred while trying to speak: {e}")

if __name__ == "__main__":
    voice_to_translation()
