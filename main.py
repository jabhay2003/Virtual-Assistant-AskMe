import speech_recognition as sr
import webbrowser
import pyttsx3


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing AskMe...")
    while True:
        # Listen for the wake word "AskMe"
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
        print("recognizing...")
        try:
            command = r.recognize_google(audio)
            print(command)
        except sr.UnknownValueError:
             print("Could not understand audio")