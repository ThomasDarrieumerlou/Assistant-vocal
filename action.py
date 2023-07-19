import openai
from conf.config import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY
from lib.init import speak_answer
from time import sleep
from src.request import run_pipeline
from src.youtube import search_bar

def taches(prompt, context=None):
    if prompt.lower().startswith("dit jarvis"):
        str = prompt.split(' ', 2)[2]

        if 'lance le pipeline r&d' in str:
            run_pipeline("nest-sonar", "r-d-devops-tools")
            sleep(5)
            response = "La demande vient d'être réaliser"
            return (response)
        
        elif 'lance le pipeline DMA' in str:
            run_pipeline("feature/pipeline-build-upload", "dmasuite")
            sleep(5)
            response = "La demande vient d'être réaliser"
            return (response)
        
        elif 'ouvre youtube' in str:
            print ("start")
            search_bar()
        else:
            return (0)
    
    elif prompt.lower().startswith("dit chatgpt"):
        str = prompt.split(' ', 2)[2]
        if context:
            prompt = context + prompt

        try:
            response = openai.Completion.create(
                model="text-davinci-003", 
                prompt=prompt, max_tokens=2048, 
            )
            response ["choices"][0]["text"]
            if response == None:
                print (response)
                response = "Une erreur s'est produits. Le programme vient de s'arrêter."
                return response
            else:
                return response
            
        except Exception as e:
            print("Error: ", e)
    
    else :
        return (0)