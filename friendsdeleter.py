import discord
import requests

user_token = input("Token-Here")

headers = {
    "Authorization": user_token
}

response = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers)

for friend in response.json():
    response = requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{friend['id']}", headers=headers)

    print(f"Status : {response.status_code}")

response = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers)

print(f"Friends: {len(response.json())}")