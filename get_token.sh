#!/bin/bash

# === URL-ENCODE FUNCTION ===
urlencode() {
  local raw="$1"
  local encoded=""
  local i c

  for (( i = 0; i < ${#raw}; i++ )); do
    c=${raw:$i:1}
    case "$c" in
      [a-zA-Z0-9.~_-]) encoded+="$c" ;;
      *) printf -v encoded '%s%%%02X' "$encoded" "'$c" ;;
    esac
  done

  echo "$encoded"
}

# === CONFIGURATION ===
TOKEN_URL="http://localhost/peoplesuite-ohrmv5/web/index.php/oauth2/token"
CLIENT_ID="229a4c5c4e14984efae60fab87aa2bdd"
RAW_CLIENT_SECRET="xMCjUiWwI6o33b+A7QaoU2OhKkfhLUv8hsMXG6s78Qw="
CLIENT_SECRET=$(urlencode "$RAW_CLIENT_SECRET")
REDIRECT_URI="http://localhost/"

# === GET CODE FROM ARGUMENT ===
AUTH_CODE="$1"

if [ -z "$AUTH_CODE" ]; then
  echo "Usage: ./get_token.sh <authorization_code>"
  exit 1
fi

# === REQUEST ACCESS TOKEN ===
RESPONSE=$(curl -s -X POST "$TOKEN_URL" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code" \
  -d "code=$AUTH_CODE" \
  -d "redirect_uri=$REDIRECT_URI" \
  -d "client_id=$CLIENT_ID" \
  -d "client_secret=$CLIENT_SECRET")

# === SAVE TO token.json ===
echo "$RESPONSE" | jq '.' > token.json

# === DISPLAY TO CONSOLE ===
echo "Tokens saved to token.json:"
cat token.json