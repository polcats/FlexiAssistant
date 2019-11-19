from speech import *
from actions import do_action
from voice import playText


def waitForCommands():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        playText("Say something!")
        guess = recognize_speech_from_mic(recognizer, microphone)
        if guess["transcription"]:
            break
        if not guess["success"]:
            break
        playText("I didn't catch that. What did you say?")

    if guess["error"]:
        print("ERROR: {}".format(guess["error"]))

    playText("You said: {}".format(guess["transcription"]))

    action = do_action(guess["transcription"].lower())

    return action


flag = True
while flag:
    flag = waitForCommands()
