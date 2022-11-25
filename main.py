import os
import requests
import webbrowser
import json
import time
from Config.tokens import *
from Controllers.api_controller import *
from Controllers.notification_controller import *

def main():

    secs = 60
    times = 0

    print("Which streamer do you want to check?", flush=True)
    twitch_user = input("Twitch username: ")

    try:
        userdata = check_user(twitch_user)
    except:
        main()

    if(userdata):
        while True:
            streamer_info = getting_data_from_streamer(userdata, twitch_user)

            if streamer_info == 0:
                time.sleep(5)
            else:
                notify(streamer_info, twitch_user)
                time.sleep(secs)
                times+=1
                print(times)

                if times > 5:
                    secs = secs * 2
    

if __name__ == "__main__":
    secs = 60
    times = 0

    while True:
        main()
        # time.sleep(60)