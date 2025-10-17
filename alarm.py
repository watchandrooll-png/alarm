import datetime
from playsound import playsound
import time
import math

while True:
    alarmer = input("In how many hours do you want the alarm to go off at?\nChoice: ")
    tim = datetime.datetime.now()
    minute = tim.minute
    hour = float(tim.hour) + (minute / 100) 
    timetoalert = float(alarmer) + hour
    while True:
        tim = datetime.datetime.now()
        minute = tim.minute
        hour = float(tim.hour) + (minute / 100)
        print(hour)
        print(timetoalert)
        if timetoalert <= hour:
            playsound("preview.mp3")
            break
        time.sleep(1)

