from pyttsx3 import engine
import wikipedia
import pyttsx3
import speech_recognition as sr
import time

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[6].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def speak():
    mic = sr.Microphone(device_index=1)
    with mic as source:
        time.sleep(0.25)
        r.adjust_for_ambient_noise(source)
        global audio
        audio = r.record(source=mic, duration=10)


text = "Type your topic or Press Enter to speak: "
talk(text)
question = input(text)
if question == "":
    text1 = "Say your topic! You have 10 seconds."
    talk(text1)
    print(text1)
    speak()
    try:
        text = "I heard " + r.recognize_google(audio) + ", is that correct? "
        talk(text)
        correct_audio = input(text)
        if correct_audio == "yes" or correct_audio == "y":
            pass
        elif correct_audio == "no":
            print("Sorry, try again later")
            quit()
        else:
            print("Sorry, try again later")
            quit()
    except sr.UnknownValueError:
        print("Sorry, we could not understand your audio")
    except sr.RequestError as e:
        print("Error: {0}".format(e))
else:
    pass

category = input(
    "Type which category your topic is in for a better result (or press enter to speak): ")
if question == "":
    text1 = "Say your topic! You have 10 seconds."
    talk(text1)
    print(text1)
    speak()
    try:
        text = "I heard " + r.recognize_google(audio) + ", is that correct? "
        talk(text)
        correct_audio = input(text)
        if correct_audio == "yes" or correct_audio == "y":
            pass
        elif correct_audio == "no":
            print("Sorry, try again later")
            quit()
        else:
            print("Sorry, try again later")
            quit()
    except sr.UnknownValueError:
        print("Sorry, we could not understand your audio")
    except sr.RequestError as e:
        print("Error: {0}".format(e))
else:
    pass


lang = "en"

# if lang == "english":
#     lang = "en"
# elif lang == "spanish" or text == "espanol":
#     lang = "es"
# elif lang == "french":
#     lang = "fr"
# else:
#     pass

question = f"{str(question)} ({category.lower()})"
try:
    wikipedia.set_lang(lang)
    answer = wikipedia.summary(question)

    print(answer)

    talk(answer)
except:
    text = "Sorry, that topic is unavailable."
    talk(text)
    print(text)
