import os
# Use the package we installed
from slack_bolt import App
from spotify import get_spotify_currently_song
from time import sleep
from datetime import datetime


USER = os.environ.get('SLACK_USER_ID')
# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_USER_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


# Add functionality here
@app.command("/start_spotify_sharing")
def update_home_tab(ack, say, client, logger):
    ack()

    while True:
        currently_song, currently_artist = get_spotify_currently_song()
        try:
            # views.publish is the method that your app uses to push a view to the Home tab
            client.users_profile_set(
                user=USER,
                profile={
                    "status_text": f"{currently_song} by {currently_artist}",
                    "status_emoji": ":spotify:",
                    "status_expiration": datetime.now().timestamp() + 300
                }
            )
        except Exception as e:
            logger.error(f"Error publishing home tab: {e}")

        sleep(5)


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
