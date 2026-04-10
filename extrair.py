from json import load
import os
import requests
from constantes import URL_BASE
from dotenv import load_dotenv
import pprint

load_dotenv()
# import pdb; pdb.set_trace()

def get_endpoint(endpoint, endpoint_id=None, params=None):
    
    headers = {
        "Accept": "application/json",
        "APP_ID": os.environ["APP_ID"],
        "APP_KEY": os.environ["APP_KEY"],
        "ResourceVersion": "v4"
    }
    if endpoint and endpoint_id:
        url = f"{URL_BASE}/{endpoint}/{endpoint_id}"
    elif endpoint and endpoint_id and params:
        url = f"{URL_BASE}/{endpoint}/{endpoint_id}/?{params}"
    elif endpoint:
        url = f"{URL_BASE}/{endpoint}"
    else:
        raise ValueError("Endpoint is required")
    response = requests.get(url, headers=headers, params=None)
    return response.json()
    
if __name__ == "__main__":
    pprint.pprint(get_endpoint("airlines"))