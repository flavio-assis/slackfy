import spotipy
from spotipy.oauth2 import SpotifyOAuth


class Player:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.scope = "user-read-playback-state"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            scope=self.scope,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
        ))

    def get_current_track(self):
        results = self.sp.current_user_playing_track()
        track = results.get('item', {}).get('name')
        artists = [artist.get('name') for artist in results.get('item', {}).get('artists', [])]
        is_playing = results.get('is_playing', False)
        return track, artists, is_playing
