from django.shortcuts import render

# Create your views here.
import requests
import json

from django.http import HttpResponse
def foo(request):
    user_information = requests.get('http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=28B545A03D3F44B20B76CA6AA8D52FF9&steamids=76561198110364054')
    matches = requests.get('https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v001/?key=28B545A03D3F44B20B76CA6AA8D52FF9&steamid=76561198110364054')
    match_prints = []
    for match in json.loads(matches.text)['result']['matches']:
        print(match['match_id'])
        match_details = requests.get('https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?match_id=%s?key=28B545A03D3F44B20B76CA6AA8D52FF9&steamid=76561198110364054' % str(match['match_id']) )
1506534909
        match_prints.append(match_details)

    return HttpResponse(match_prints)