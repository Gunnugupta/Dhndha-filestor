import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

AUTH_CHANNEL = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('AUTH_CHANNEL', '-1002237286662').split()] 


UPDATE = environ.get("SUPPORT", "")
SUPPORT = environ.get("SUPPORT", "")
OWNERID = int(environ.get("OWNERID" ,"6359874284"))
YT = environ.get("YT", "")

# Bot Information
API_ID = int(environ.get("API_ID", "25492855"))
API_HASH = environ.get("API_HASH", "61876db014de51a4ace6b169608be4f1")
BOT_TOKEN = environ.get("BOT_TOKEN", "nUbAA-nNBQ")

PICS = (environ.get('PICS', 'https://graph.org/file/34384a407532bf5738721.jpg')).split() # Bot Start Picture
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6359874284').split()]
BOT_USERNAME = environ.get("BOT_USERNAME", "FileShare_Hgbot") # without @
PORT = environ.get("PORT", "8080")

# Clone Info :-
CLONE_MODE = bool(environ.get('CLONE_MODE', True)) # Set True or False

# If Clone Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
CLONE_DB_URI = environ.get("CLONE_DB_URI", "")
CDB_NAME = environ.get("CDB_NAME", "HGBOTZ")

# Database Information
DB_URI = environ.get("DB_URI", "mongodbue&wCluster0")
DB_NAME = environ.get("DB_NAME", "HGBOTZ")

# Auto Delete Information
AUTO_DELETE_MODE = bool(environ.get('AUTO_DELETE_MODE', True)) # Set True or False

# If Auto Delete Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800")) # Time in Seconds

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002155023199"))

# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable - True or Disable - False
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# Verify Info :-
VERIFY_MODE = bool(environ.get('VERIFY_MODE', False)) # Set True or False

# If Verify Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
SHORTLINK_URL = environ.get("SHORTLINK_URL", "") # shortlink domain without https://
SHORTLINK_API = environ.get("SHORTLINK_API", "") # shortlink api
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/ultroid_official/18") # how to open link 

# Website Info:
WEBSITE_URL_MODE = bool(environ.get('WEBSITE_URL_MODE', False)) # Set True or False

# If Website Url Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
WEBSITE_URL = environ.get("WEBSITE_URL", "") # For More Information Check Video On Yt - @PhdLust

# File Stream Config
STREAM_MODE = bool(environ.get('STREAM_MODE', False)) # Set True or False

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://testofuxbfilter-1fa60b1b8498.herokuapp.com/")

