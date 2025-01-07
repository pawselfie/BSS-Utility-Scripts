# This script serves as a complex autoposter that won't get you caught, and will send any message you specify in random intervals

import requests # Make sure you run 'pip install requests' as request module is not installed by default
import time
import random # Make sure you run 'pip install random' as request module is not installed by default

url = "url" # Url to the channel you want to autopost in

payload = {
    "content" : "text" # Message you want to send
}

headers = {
    "Authorization" : "token" # Your discord authorization token (find a tutorial online if you dont know where to get it)
}

# This code simulates how humans post, by waiting random intervals, then taking a 30-35 min break after some time, to then continue autoposting
# It is pretty much undetectable and works well on trading channels where there's a message every 10 min or so

y = 1
z = 4
a = 10
b = 1
c = 1
f = 1
n = 1
while True:
    while y <= a:
        b = random.randint(1, 15)
        if n == b:
            b = b + random.randint(1, 3)
        c = random.random()
        t = z + random.randint(1, 3)
        f = (t*150) + b
        n = b
        requests.post(url, payload, headers=headers)
        time.sleep(f)
        time.sleep(c)
        y = y + 1
        a = 16 - random.randint(1, 7)
    time.sleep(random.randint(1800, 2100))
    y = 1