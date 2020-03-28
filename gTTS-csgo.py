from gtts import gTTS
import gtts
import os
from playsound import playsound
import tempfile

LANGUAGES = [language for language in gtts.lang.tts_langs()]
COMMAND = ".say"
print(LANGUAGES)

# open log file. EX: C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\gtts.log when con_logfile "gtts.log"
FO = open('', 'r', encoding='utf8')
FO.seek(0, 2)
print("reading file")


def TTS(message, language):
    tts = gTTS(text=message, lang=language)

    # Set a directory if you want
    name = tempfile.mktemp(suffix='.mp3', dir='')
    tts.save(name)
    playsound(name)
    os.remove(name)


def splicer(mystr, sub):
    index = mystr.find(sub)
    if index != -1:
        return mystr[index:]
    else:
        pass


while True:
    loglines = FO.readline()
    if COMMAND in loglines:
        print(loglines)
        string = splicer(loglines, COMMAND)
        string2 = string.split()
        print(string2)

        Language = "en"
        if len(string2[0]) > 4:
            Language = string2[0][4:]
            print(Language)

        if Language not in LANGUAGES:
            print("Language not available")
            continue

        if string[len(string2[0]):].isspace():
            print("No input found")
            continue

        print(string[len(string2[0]):])
        TTS(string[len(string2[0]):], Language)
