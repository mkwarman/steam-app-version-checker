import settings
from os import path
from requests import get, post

def get_local_version():
    if not path.exists(settings.VERSION_FILE_PATH):
        open(settings.VERSION_FILE_PATH, 'w').close()
        return None

    with open (settings.VERSION_FILE_PATH, 'r') as f:
        current_version = f.readline().rstrip('\n')

    return current_version


def get_remote_version():
    json_response = get(settings.STEAM_API_URL + settings.APP_ID).json()
    remote_version = json_response['data'][settings.APP_ID]['depots']['branches']['public']['buildid']
    return remote_version


def save_version(new_version):
    with open (settings.VERSION_FILE_PATH, 'w') as f:
        f.write(new_version)


def send_discord(new_version):
    message = (settings.DISCORD_MESSAGE.format(new_version))
    post_data = {
        'content': message,
        'allowed_mentions': {
            'parse': ['users']
        }
    }
    post(settings.DISCORD_WEBHOOK_URL, json=post_data)


def send_push(new_version):
    message = (settings.PUSH_MESSAGE.format(new_version))
    post_data = {
        "token": settings.PUSH_APP_TOKEN,
        "user": settings.PUSH_USER_KEY,
        "message": message,
        "title": settings.PUSH_TITLE
    }
    post(settings.PUSHOVER_API_URL, json=post_data)


if (__name__ == '__main__'):
    local_version = get_local_version()
    remote_version = get_remote_version()

    if (local_version != remote_version):
        save_version(remote_version)
        send_discord(remote_version)
        send_push(remote_version)
