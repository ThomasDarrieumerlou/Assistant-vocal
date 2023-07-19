from lib.read import read_prompt
from src.assistant_vocal import listen_speecher, reconnaissance_vocale
import requests
import json

def search_bar():
    while True:
        read_prompt("Veuillez renseigner la video que vous voulez lire")
        print ("deuxième étape")
        recorded_audio = listen_speecher()
        prompt = reconnaissance_vocale(recorded_audio)

        prompt = "i kendrick lamar"

        if prompt is None:
            continue
        elif prompt.lower() == "stop":
            response = "Youtube vient d'être fermer"
            return (response)
        else:
            youtube_request(prompt)
            return (0)

def youtube_request(prompt):
    url = "https://www.googleapis.com/youtube/v3/search"
    api_key = ''
    
    params = {
        'part': 'snippet',
        'q': prompt,
        'type': 'video',
        'key': api_key,
        'maxResults': 1
    }

    response = requests.request ("GET", url, params=params)
    print(response.status_code)
    data = response.json()

    if 'items' in data and len(data['items']) > 0:
        video_id = data['items'][0]['id']['videoId']
        play_video(video_id, prompt)
    else:
        return None
    


def play_video(video_id, prompt):
    if video_id:
        url =f'https://www.youtube.com/watch?v={video_id}'
        print(f"Vou écoutez: {prompt}")
    else:
        print("Aucune video trouvée pour cette recherche")