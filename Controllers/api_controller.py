import os
import requests
import webbrowser
import json
import time
from Config.tokens import *

TOKEN = get_token()

def getting_user_data(twitch_user):
    url = f'https://api.twitch.tv/helix/users?login={twitch_user}'
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Client-Id': f'{CLIENT_ID}'}

    try:
        req = requests.get(url=url, headers=headers)
        userdata = req.json()
        return userdata

    except:
        print("Failed to get the user data.", flush=True)

def check_user(twitch_user):
    userdata = getting_user_data(twitch_user)

    if len(userdata['data']) == 0:
        print(f"The username '{twitch_user}' doesn't exist.", flush=True)
    else:
        return userdata

def getting_stream_info(userdata):
    img = userdata['data'][0]['profile_image_url']
    user_id = userdata['data'][0]['id']

    url = f'https://api.twitch.tv/helix/streams?user_id={user_id}'
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Client-Id': f'{CLIENT_ID}'}

    try:
        req = requests.get(url=url, headers=headers)
        stream_info = req.json()
        stream_info.update({'img': img})
        return stream_info

    except:
        print("Failed to get the stream info.", flush=True)

def getting_data_from_streamer(userdata, twitch_user):
    stream_info = getting_stream_info(userdata)

    if len(stream_info['data']) == 0:
        print(f"{twitch_user} isn't currently live :(", flush=True)
        return 0
        
    else:
        streamer_url = f"https://www.twitch.tv/{twitch_user}"

        title = stream_info['data'][0]['title']
        id_streamer = stream_info['data'][0]['id']
        img = stream_info['img']

        streamer_info = {
            'title': title,
            'streamer_url': streamer_url,
            'user': twitch_user,
            'img': img,
            'id_streamer': id_streamer
        }
        return streamer_info