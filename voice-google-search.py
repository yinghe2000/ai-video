import speech_recognition as sr
from googlesearch import search

# Function to record speech and return as text
def voice_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Function to perform a Google search
def google_search(query):
    for j in search(query, num=10, stop=10, pause=2):
        print(j)

# Main function
def main():
    query = voice_to_text()
    if query:
        google_search(query)

if __name__ == "__main__":
    main()

