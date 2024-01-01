import requests
import pyfiglet

def print_ascii_art(text):
    ascii_art = pyfiglet.figlet_format(text, font="slant")
    print(ascii_art)

title = "Minecraft UUID Checker"
print_ascii_art(title)

def get_player_uuid(username):
    base_url = "https://api.mojang.com/users/profiles/minecraft/"
    url = f"{base_url}{username}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['id']
        else:
            print(f"Failed to get UUID for player {username}. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request failed: {str(e)}")
        return None

while True:
    player_username = input("Please Input Player ID:")
    uuid = get_player_uuid(player_username)
    print(f"The UUID of player '{player_username}' is: {uuid}")
