# Created on 08/12/2024

# This is a util that generates a free key for the DeArrow browser extension, this bypasses the requirement to get this key after "waiting up to 12 hours".
# This API was found after I reverse engineered DeArrow's chrome extension for fun.
# This was very fun to do, but please considering supporting the creator of DeArrow if you wish to use their tool.
# You can support them here: https://dearrow.ajay.app/payment/

import requests
import json
from pyperclip import copy
from datetime import datetime

def generate_api_key() -> str:

    """
    Function that generates a free key from the DeArrow API.
    REQUIRES: N/A
    RETURNS api_key: str
    """
    API_KEY = "https://sponsor.ajay.app/api/generateToken/free"
    HEADERS = {"Content-Type": "application/json"}
    DATE_TIME = int(datetime.now().timestamp() * 1000)
    PARAMS = {"key": DATE_TIME}

    request = requests.get(url=API_KEY, params=PARAMS, headers=HEADERS)
    if request.status_code != 200:
        raise ValueError("API response gave an invalid status code of " + str(request.status_code))
    
    request_json = json.loads(request.text)
    key = request_json.get("licenseKey")
    return key
key =  generate_api_key()
copy(key)
print("Your DeArrow generated key is: " + key)
print("Your key has been copied into your clipboard for easy use!")
input("Press enter to exit...")