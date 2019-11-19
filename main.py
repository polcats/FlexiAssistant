
from speech import *
from actions import *


def waitForCommands():
    word = "testing"
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

    guess_is_correct = do_action(guess["transcription"].lower())

    if guess_is_correct:
        print("Correct! You win!".format(word))
    elif guess["transcription"] == "exit".lower():
        return False
    else:
        print("Sorry, you lose!\nI was thinking of '{}'.".format(word))

    return True


flag = True
while flag:
    flag = waitForCommands()
