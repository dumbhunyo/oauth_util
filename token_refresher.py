import json
import requests
import urllib.parse
from datetime import datetime
import os

# === CONFIGURATION ===
token_file = os.path.join(os.path.dirname(__file__), 'token.json')
refresh_log = os.path.join(os.path.dirname(__file__), 'refresh_log.txt')

client_id = '229a4c5c4e14984efae60fab87aa2bdd'
client_secret = 'xMCjUiWwI6o33b+A7QaoU2OhKkfhLUv8hsMXG6s78Qw='
token_url = 'http://localhost/peoplesuite-ohrmv5/web/index.php/oauth2/token'


# === Load tokens from token.json ===
def load_tokens(path):
    with open(path, 'r') as f:
        return json.load(f)


# === Save tokens to token.json ===
def save_tokens(path, tokens):
    with open(path, 'w') as f:
        json.dump(tokens, f, indent=2)


# === Refresh access token using refresh_token ===
def refresh_access_token(refresh_token, client_id, client_secret, token_url):

    # Prepare POST data
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret 
    }


    # Send POST request to token endpoint
    response = requests.post(token_url, data=data)

    # Raise exception if server returns error status
    response.raise_for_status()

    # Parse JSON response
    return response.json()


# === Main execution ===
try:
    tokens = load_tokens(token_file)
    new_tokens = refresh_access_token(tokens['refresh_token'], client_id, client_secret, token_url)

    # Check if response contains a new access token
    if 'access_token' in new_tokens:
        save_tokens(token_file, new_tokens)
        print("Access token refreshed successfully.")
        print(json.dumps(new_tokens, indent=2))

        # Log refresh time to file
        with open(refresh_log, 'a') as log:
            log.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Token refreshed\n")
    else:
        print("Failed to refresh token:", new_tokens)

except Exception as e:
    print("Error refreshing token:", str(e))