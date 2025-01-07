# This script sends a "FollowTo MountainTop" to any channel you specify at any time of the hour
# Use it with a guide-atk alt to throw it at mondo by xx:57
# You can change the time var to throw the alt on mtop whenever you wish
# Configure the duration using aqts alt sync
# Reccommendation: Use a custom pattern in Mtop to not die to mondo

import requests # Make sure to run 'pip install requests' as requests module is not installed in python by default
import time
import datetime


time = 57  # This determines the minute when the script will send the FollowTo
url = "url"  # This is the webhook url
payload = {
    "content" : "FollowTo MountainTop"
}

while True:
    time.sleep(0.1)
    now = int(time.time())
    date = datetime.datetime.fromtimestamp(now)
    min = str(date)
    minutes = min[14] + min[15]
    if int(minutes) == time:
        requests.post(url, payload)
        print("Hour: "+min[11]+min[12]+", sent command to go to mtop.")
        time.sleep(70)
