import time
import requests
from winotify import Notification, audio

def getting_profile_image(info, username): 
    with open(f'./Data/image.jpg', 'wb') as f:
                f.write(requests.get(info['img']).content)

def notify(info, username):
    getting_profile_image(info, username)
    toast = Notification("Is Live?",
                         info['user'] + " is live :)",
                         info["title"], 
                         r"C:\Users\ferna\workspace\is-live-on-twitch\Data\image.jpg")
                         
    
    toast.add_actions(label="Go to the stream!", launch=info["streamer_url"])  

    toast.show()

    return 1