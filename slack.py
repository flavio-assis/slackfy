from datetime import datetime

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class Status:
    def __init__(self, token, user_id):
        self.client = WebClient(token=token)
        self.user_id = user_id

    def update_slack_status(self, status_text, status_emoji, expiration=300):
        try:
            response = self.client.users_profile_set(
                user=self.user_id,
                profile={
                    "status_text": status_text,
                    "status_emoji": status_emoji,
                    "status_expiration": int(datetime.now().timestamp()) + expiration  # 5 minutes
                }
            )
        except SlackApiError as e:
            pass
