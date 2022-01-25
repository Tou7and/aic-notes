""" Test Client

Usage: 
    Start a RASA server at localhost:5005
    python rasa_client.py [TEXT]
"""
import sys
import requests
import json

if __name__ == "__main__":
    url = 'http://localhost:5005/webhooks/rest/webhook'
    msg = str(sys.argv[1])

    data = {
        'sender': "test_user1",
        'message': msg
    }

    try:
        r = requests.post(url, data=json.dumps(data))
    except:
        print("Failed to link {}".format(url))
        sys.exit()
    if r.status_code != 200:
        print("Error status: {}".format(r.status_code))
    else:
        result = r.text
        result = json.loads(result)
        print(result[0])
