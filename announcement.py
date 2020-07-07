import json
import datetime
import time
import math
import requests
import httplib2 as http  # External library
from urllib.parse import urlparse
import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 125)  # setting up new voice rate

while True:

    now = datetime.datetime.now()
    Time = now.strftime("%H %M")
    hour = now.hour
    city = 'singapore'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=8bbaa9aac07b8b7aee5d54eee1e7cfdd&units=metric'.format(
        city)
    res = requests.get(url)
    data = res.json()
    description = data['weather'][0]['description']
    print(description)

    engine.say("The time now is" + Time)
    engine.say("The current weather forecast")
    engine.say(description)

    if __name__ == "__main__":
        # Authentication parameters
        headers = {'AccountKey': 'NXpFdS3XQnqaH4jIc2g6kQ==',
                   'accept': 'application/json'}  # this is by default

        # API parameters
        uri = 'http://datamall2.mytransport.sg/'  # Resource URL
        path = 'ltaodataservice/BusArrivalv2?BusStopCode=75279'

    # Build query string & specify type of API call
    target = urlparse(uri + path)
    method = 'GET'
    body = ''

    # Get handle to http
    h = http.Http()

    # Obtain results
    response, content = h.request(target.geturl(), method, body, headers)

    # Parse JSON to print
    jsonObj = json.loads(content)

    z = len(jsonObj['Services'])

    BusService = ['', '', '', '', '']
    firstBus = ['', '', '', '', '']
    Bus1 = ['', '', '', '', '']
    BusTiming1 = ['', '', '', '', '']
    BusArr1 = ['', '', '', '', '']
    min1 = ['', '', '', '', '']

    for x in range(z):
        BusService[x] = jsonObj['Services'][x]['ServiceNo']
        firstBus[x] = jsonObj['Services'][x]['NextBus']['EstimatedArrival']

        Bus1[x] = (firstBus[x].replace("T", " ")).replace("+08:00", "")
        BusTiming1[x] = datetime.datetime.strptime(Bus1[x], '%Y-%m-%d %H:%M:%S')
        BusArr1[x] = ((BusTiming1[x] - now).total_seconds()) / 60
        min1[x] = math.trunc(BusArr1[x])
        if min1[x] <= 1:
            min1[x] = "Arr"

        print(BusService[x])
        print(min1[x])
        print("\n")

        if BusService[x] == '72' and min1[x] == "Arr":
            engine.say("Bus seventy two arriving")

        if BusService[x] == '27' and min1[x] == "Arr":
            engine.say("Bus twenty seven arriving")

        if BusService[x] == '168' and min1[x] == "Arr":
            engine.say("Bus one six eight arriving")

        if BusService[x] == '27A' and min1[x] == "Arr":
            engine.say("Bus twenty seven a arriving")

        if BusService[x] == '127' and min1[x] == "Arr":
            engine.say("Bus one two seven arriving")

    engine.runAndWait()
    time.sleep(30)
