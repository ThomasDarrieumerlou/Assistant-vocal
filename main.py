from src.assistant_vocal import listen_speecher, reconnaissance_vocale
from lib.read import read_prompt
from time import sleep
from pygame import mixer
from src.action import taches

if __name__ == "__main__":
    mixer.init()

    while True:

        recorded_audio = listen_speecher()
        prompt = reconnaissance_vocale(recorded_audio)

        prompt = "dit Jarvis ouvre youtube"
        print (prompt)

        if prompt is None:
            continue
        elif prompt.lower() == "exit":
            break
        else :
            response_text = taches(prompt)
            if response_text == 0 or response_text == None:
                print ("aucune informations n'a étés demandées ou pris en charge")
                continue
            else :
                read_prompt(response_text)
        while mixer.get_busy():
            sleep(0.1)

    mixer.quit()