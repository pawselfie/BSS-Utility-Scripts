# This script serves as a simple autoposter, and will send any message you specify every 2 minutes

import requests # Make sure you run 'pip install requests' as request module is not installed by default
import time

url = "url" # Url to the channel you want to autopost in

payload = {
    "content" : "text" # Message you want to send
}

headers = {
    "Authorization" : "token" # Your discord authorization token (find a tutorial online if you dont know where to get it)
}

while True:
    requests.post(url, payload, headers=headers)
    time.sleep(120.5) # Time to wait between each send, 2 minutes and half a second by default
