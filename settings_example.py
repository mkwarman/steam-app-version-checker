# Path to version file. If this file does not exist it will be created
VERSION_FILE_PATH = '_current_valheim_server_version'

# Steam API. Note that we're using SteamCMD rather than steam's actual API
STEAM_API_URL = "https://api.steamcmd.net/v1/info/"

# App id to monitor - Sample APP_ID is Valheim Dedicated Server
APP_ID = '896660'

# Webhook for discord messages (https://discord.com/)
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/my_web_hook"

# Message to post in Discord. Build number will be given via format
DISCORD_MESSAGE = "There is a new version of the Valheim Dedicated Server available (build {0})"

# URL for Pushover POSTs (https://pushover.net)
PUSHOVER_API_URL = "https://api.pushover.net/1/messages.json"

# Pushover user key
PUSH_USER_KEY = 'xyzxyzxyzxyzxyzxyzxyz'

# Pushover app token
PUSH_APP_TOKEN = 'xyzxyzxyzxyzxyzxyzxyz'

# Push notification title
PUSH_TITLE = "New Valheim Server Version"

# Push notification message
PUSH_MESSAGE = "There is a new version of the Valheim Dedicated Server available (build {0})"