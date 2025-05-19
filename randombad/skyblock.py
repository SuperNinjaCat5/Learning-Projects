import requests
import os

API_KEY = "ea8e6109-9fd5-481b-b7b9-c7194d3a1515"

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_player_uuid():
    player_name = input("Enter player's username: ")
    url = f"https://api.mojang.com/users/profiles/minecraft/{player_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["id"]
    else:
        print("Failed to get player UUID.")
        return None

def get_player_profiles(uuid):
    url = f"https://api.hypixel.net/v2/player?uuid={uuid}"
    headers = {"API-Key": API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        profiles = data.get("player", {}).get("stats", {}).get("SkyBlock", {}).get("profiles", {})
        return list(profiles.keys())
    else:
        print("Failed to fetch player profiles.")
        return []

def get_skyblock_profile(profile_id):
    url = f"https://api.hypixel.net/v2/skyblock/profile?profile={profile_id}"
    headers = {"API-Key": API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch SkyBlock profile data.")
        return None

def extract_skills(profile_data, uuid):
    member_data = profile_data.get("profile", {}).get("members", {}).get(uuid, {})
    skills = {}
    skill_keys = [
        "mining", "farming", "combat", "fishing",
        "enchanting", "alchemy", "taming", "foraging"
    ]
    for skill in skill_keys:
        xp = member_data.get(f"experience_skill_{skill}", 0)
        skills[skill] = xp
    return skills

class Player:
    def __init__(self, skills, collections):
        self.skills = skills
        self.collections = collections

    def get_skill(self):
        print("Skills:")
        for skill, xp in self.skills.items():
            print(f"  {skill.capitalize()}: {xp} XP")

    def get_collections(self):
        print(f"Collections: {self.collections}")

if __name__ == "__main__":
    clear_console()
    uuid = get_player_uuid()
    if uuid:
        profile_ids = get_player_profiles(uuid)
        if profile_ids:
            # For simplicity, we'll use the first profile ID
            profile_data = get_skyblock_profile(profile_ids[0])
            if profile_data:
                skills = extract_skills(profile_data, uuid)
                player_current = Player(skills, "No collections yet")
                player_current.get_skill()
                player_current.get_collections()
            else:
                print("No profile data found.")
        else:
            print("No profiles found for this player.")


class Player:
    def __init__(self, skills, collections):
        self.skills = skills
        self.collections = collections

    def get_skill(self):
        print("Skills:")
        for skill, xp in self.skills.items():
            print(f"  {skill.capitalize()}: {xp} XP")

    def get_collections(self):
        print(f"Collections: {self.collections}")

if __name__ == "__main__":
    clear_console()
    uuid = get_player_uuid()
    if uuid:
        profile_ids = get_player_profiles(uuid)
        if profile_ids:
            # For simplicity, we'll use the first profile ID
            profile_data = get_skyblock_profile(profile_ids[0])
            if profile_data:
                skills = extract_skills(profile_data, uuid)
                player_current = Player(skills, "No collections yet")
                player_current.get_skill()
                player_current.get_collections()
            else:
                print("No profile data found.")
        else:
            print("No profiles found for this player.")
