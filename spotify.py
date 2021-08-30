import os
import requests


def get_spotify_currently_song():
    SPOTIFY_TOKEN = os.environ.get('SPOTIFY_TOKEN')
    SLACK_API_URI = 'https://api.spotify.com/v1/me/player/currently-playing'

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {SPOTIFY_TOKEN}'
    }

    try:
        res = requests.get(url=f'{SLACK_API_URI}?market=BR', headers=headers)

        if res.status_code == 204:
            return "Nothing", "No one"

        song = res.json()['item']['name']
        artist = res.json()['item']['artists'][0]['name']
        return song, artist
    except Exception as err:
        print(f'An error occurred during the request to Spotify currently song: {err}')


if __name__ == '__main__':
    print(get_spotify_currently_song())
