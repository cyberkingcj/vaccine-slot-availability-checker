#cyberkingcj
import time
import winsound
from request_json import *
from inputs import *
from os import system


request_no = 0
availablility = False

while True:
    responses = request_json()
    request_no += 1
    _ = system('cls')
    print("Searching for available slots. Loop:",request_no)
    winsound.Beep(600,200)
    for response in responses:
        for center in response.json()['centers']:
            for session in center['sessions']:
                if session['available_capacity'] > 0 and session['min_age_limit'] == age:
                    availablility = True
    if availablility == True:
        winsound.Beep(600,10000)
    else:
        print("No slots found, Trying again in ",t," seconds\n\n\n\n\n\nTo stop this app, just close this console window")
        winsound.Beep(400,200)
    time.sleep(t)
    