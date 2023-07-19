import speech_recognition as sr
from gtts import gTTS
from pygame import mixer


def speak_answer(text):
    mixer.init()
    tts = gTTS(text=text, lang='fr')
    tts.save("speech.mp3")
    sound = mixer.Sound("speech.mp3")
    sound.play()

recognizer = sr.Recognizer()
