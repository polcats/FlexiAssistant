from gtts import gTTS
import playsound
import os


def playText(text):
    file_name = "command.mp3"
    myobj = gTTS(text=text, lang='en', slow=False)
    myobj.save(file_name)
    playsound.playsound(file_name, True)
    os.remove(file_name)
