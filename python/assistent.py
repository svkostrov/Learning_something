import os
import pyttsx3


def talk(words):
    print(words)
    os.system('espeak ' + words)

talk("Ask_me_somthing")


engine = pyttsx3.init()
engine.say("Hello word")
engine.runAndWait()