#!/bin/bash

# Access Token
ACCESS_TOKEN="def5020032e4795d98a933a87571295ccda64ef56b66226df5fde9ca48408d8d74ba7f262a7db0796fa9763cf26f9c723a860bcd6853fa8686454c34a17cdced90be0bea564aa8437d605308f692e2d8c931fceb97f29b6db34e8cc1ec6e95e80afa7aef9d6b8a4e546d88b4738467fbd21d99d597fa9baef1c579cfbf063d5d0362da7988e62024b319bd60afb61d6733a222758fc698622e6f7ca6b3723c9f4d493eef"

# Request
curl -X GET "http://localhost/peoplesuite-ohrmv5/web/index.php/api/v2/attendance/timezones" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $ACCESS_TOKEN"