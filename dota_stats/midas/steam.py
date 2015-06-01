
import requests

class SteamImporter():
    matches = requests.get('http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=440&count=3&maxlength=300&format=json', headers={'Content-type: application/json'})
    print matches.text


