import speech_recognition as sr
import webbrowser

def voice_search():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as source for input
    with sr.Microphone() as source:
        print("Say something to search...")
        audio = recognizer.listen(source)

    # Recognize speech using Google Speech Recognition
    try:
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        # Use the query for searching; here, we're using Google Search
        webbrowser.open(f"https://www.google.com/search?q={query}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# Run the voice search function
voice_search()

