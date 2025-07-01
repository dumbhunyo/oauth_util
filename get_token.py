import sys
import json
import requests
import urllib.parse

# === CONFIGURATION ===
TOKEN_URL = "http://localhost/peoplesuite-ohrmv5/web/index.php/oauth2/token"
CLIENT_ID = "229a4c5c4e14984efae60fab87aa2bdd"
CLIENT_SECRET = "xMCjUiWwI6o33b+A7QaoU2OhKkfhLUv8hsMXG6s78Qw="
REDIRECT_URI = "http://localhost/"

# === GET CODE FROM ARGUMENT ===
if len(sys.argv) != 2:
    print("Usage: python3 get_token.py <authorization_code>")
    sys.exit(1)

AUTH_CODE = sys.argv[1]

# === REQUEST ACCESS TOKEN ===
data = {
    "grant_type": "authorization_code",
    "code": AUTH_CODE,
    "redirect_uri": REDIRECT_URI,
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(TOKEN_URL, data=data, headers=headers)

# === SAVE TO token.json ===
with open("token.json", "w") as f:
    json.dump(response.json(), f, indent=2)

# === DISPLAY TO CONSOLE ===
print("Tokens saved to token.json:")
print(json.dumps(response.json(), indent=2))