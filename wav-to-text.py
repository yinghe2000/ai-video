import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Load your .wav file
with sr.AudioFile('./harvard.wav') as source:
    # Listen for the data (load audio to memory)
    audio_data = recognizer.record(source)
    # Recognize (convert from speech to text)
    try:
        text = recognizer.recognize_google(audio_data)
        print(text)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

