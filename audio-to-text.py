import speech_recognition as sr
from pydub import AudioSegment
import os

def audio_to_text(audio_file):
    # Convert audio to the required format
    sound = AudioSegment.from_file(audio_file)
    audio_file = "converted.wav"
    sound.export(audio_file, format="wav")

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

        # Convert audio to text
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand the audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

def search_text_in_audio(audio_file, search_query):
    text = audio_to_text(audio_file)
    return search_query in text

# Usage Example
audio_file_path = "path/to/your/audiofile.extension"  # Replace with your audio file path
search_query = "text to search"
result = search_text_in_audio(audio_file_path, search_query)
print(f"Is '{search_query}' in the audio? {'Yes' if result else 'No'}")
