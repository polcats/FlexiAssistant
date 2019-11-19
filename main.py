
from speech import *
from actions import do_action


def waitForCommands():
    PROMPT_LIMIT = 5
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    for j in range(PROMPT_LIMIT):
        print("Say something!")
        guess = recognize_speech_from_mic(recognizer, microphone)
        if guess["transcription"]:
            break
        if not guess["success"]:
            break
        print("I didn't catch that. What did you say?\n")

    if guess["error"]:
        print("ERROR: {}".format(guess["error"]))

    print("You said: {}".format(guess["transcription"]))

    action = do_action(guess["transcription"].lower())

    return action


flag = True
while flag:
    flag = waitForCommands()
