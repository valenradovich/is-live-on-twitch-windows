import os
import requests
import webbrowser
import json

CLIENT_ID = "xxx"
CLIENT_SECRET = "xxx"

def get_token():
    url = 'https://id.twitch.tv/oauth2/token'

    params = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type':'client_credentials'}

    try:
        req = requests.post(url=url,params=params)
        token = req.json()['access_token']

        return token

    except:
        print("Failed to get the token.", flush=True)
