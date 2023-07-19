import requests
import json

def run_pipeline(branch, repo):

    if repo == "dmasuite":
        AUTH = "Bearer ATCTT3xFfGN0LV_6GL1ymSEXSJuGXL9yOtn_oHJKqaWkpKWXNP13DAY-s6LKFURifC7FWMRPYNMcyujdfyUiJ02AWriZJU0SDAB4DC6xk5sec2YCutl9Bcn6BWsJSusKB8Uo-xI8N_MmnFvjsQ16qmiJYIn5JW7LGIIm096IKgsxGXTdsWmSm5g=AC7A58D6"
    else :
        AUTH = "Bearer ATCTT3xFfGN04iraf5KCwf4B6MkbHOp0XJr3Dp4b1wGwK9yvyxupRY_j86e5ttWEfEIMGn058OyUYvWZDZCDF14gOMEHtgHasoRJ5hS1eSrfn3Nkad-1Qe73I0rGV8INriDBGSDuDrc7qdVbUpaLOov2tkwHqfcGDKeHhUTHHS2lDmFBZE1N_I8=E83B1CF0"

    url = "https://api.bitbucket.org/2.0/repositories/acoemgroup/{repo}/pipelines"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": AUTH
    }

    playload = json.dumps ({
        "target": {
            "ref_type": "branch",
            "type": "pipeline_ref_target",
            "ref_name": branch
        }
    })
    response = requests.request ("POST", url, data=playload, headers=headers)
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
