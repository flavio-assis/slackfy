import os
import sys
import time
from datetime import datetime

from loguru import logger

from slack import Status
from spotify import Player

logger.remove()
logger.add(sys.stdout, level="INFO")


def set_default_status(status):
    status.update_slack_status(
        status_text="",
        status_emoji=":hehe:",
        expiration=0
    )


def status_updater(player, status):
    current_track = ""
    while True:
        track, artists, is_playing = player.get_current_track()

        if not is_playing:
            logger.info("Spotify is not playing.")
            set_default_status(status)
            time.sleep(5)
            continue

        if len(track) > 25:
            track = track[:22] + "..."

        if len(artists) > 2:
            artists = artists[:2] + [" & Others"]

        current_track_updater = f"{track} - {' & '.join(artists)}"

        if current_track_updater != current_track:
            current_track = current_track_updater
            logger.info(f"Current track: {current_track_updater}")

            status.update_slack_status(
                status_text=current_track,
                status_emoji=":spotify:",
                expiration=datetime.now().timestamp() + 300
            )

        time.sleep(5)


if __name__ == '__main__':
    player = Player(
        client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
        client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=os.environ.get("SPOTIFY_REDIRECT_URI")
    )
    status = Status(
        token=os.environ.get("SLACK_USER_TOKEN"),
        user_id=os.environ.get("SLACK_USER_ID")
    )
    try:
        status_updater(player, status)
    except KeyboardInterrupt:
        logger.info("Stopping status updater. Setting default status...")
        set_default_status(status)
