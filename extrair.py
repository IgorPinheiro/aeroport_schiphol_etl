import os
import ipdb; ipdb.set_trace()

def get_endpoint(endpoint, endpoint_id=None, params=None):
    
    headers = {
        "Accept": "application/json",
        "APP_ID": os.environ["APP_ID"],
        "APP_KEY": os.environ["APP_KEY"],
        "ResourceVersion": "v4"
    }
    ipdb.set_trace()

    
if __name__ == "__main__":
    get_endpoint("flights")