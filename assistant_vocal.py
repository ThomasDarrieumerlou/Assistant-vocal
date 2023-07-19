import speech_recognition as sr
from lib.init import recognizer, speak_answer


def listen_speecher():
    with sr.Microphone() as source:
        print("Initialisation... Patientez... Parlez")

        recognizer.adjust_for_ambient_noise(source)
        recorded_audio = recognizer.listen(source)
        print("END")
    return (recorded_audio)

def reconnaissance_vocale(recorded_audio):
    try:
        prompt = recognizer.recognize_google(
            recorded_audio, 
            language="fr-FR"
        )
        print("Vous avez dit : {prompt}\n")  
    except sr.UnknownValueError:
        print("Je n'ai pas compris")
        prompt = None

    if prompt is None:
        return None
    
    return prompt