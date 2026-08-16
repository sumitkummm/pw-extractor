#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29899250"))
API_HASH = environ.get("API_HASH", "611d045796c79af3e5ddfa3d6fd536a7")
BOT_TOKEN = environ.get("BOT_TOKEN", "8877664462:AAGHi-qhgPz6hUFlxlHrmZMxcBaf4A0OSls")

OWNER = int(environ.get("OWNER", "8619029575"))
CREDIT = environ.get("CREDIT", "🤍🌸kumawat🌸🤍")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8619029575,8769333599').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8619029575,8769333599').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
