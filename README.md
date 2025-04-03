# Slack Status Updater

This repository contains a Python application that automates the process of updating a user's status on Slack.

## Features

- Automatically updates Slack status at regular intervals.
- Configurable status text and emoji.
- Uses environment variables for configuration.

## Requirements

- Python 3.6+
- `slack_sdk` library
- `python-dotenv` library

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add the following environment variables:
   ```env
   SLACK_USER_TOKEN=xoxp-your-slack-user-token
   SLACK_USER_ID=your-slack-user-id
   ```

## Usage

1. Run the application:
   ```sh
   python app.py
   ```

2. The application will update your Slack status every 5 minutes with the text "Working on a project" and the emoji ":computer:".

## Configuration

- To change the status text and emoji, modify the `update_status` function in `app.py`.

## Troubleshooting

- Ensure your `SLACK_USER_TOKEN` has the `users.profile:write` scope.
- If you encounter `not_allowed_token_type` or `missing_scope` errors, verify that your token has the correct permissions and scopes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
