import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re

url_dict = {"EPL": "9/Premier-League-Stats", "Ligue 1": "13/Ligue-1-Stats",
            "Bundesliga": "20/Bundesliga-Stats", "Serie A": "11/Serie-A-Stats", "La Liga": "12/La-Liga-Stats"}
league_dict = {"EPL": "s10728", "Ligue 1": "s10732",
               "Bundesliga": "s10737", "Serie A": "s10730", "La Liga": "s10731"}
player_file_dict = {"EPL": "playerstats_epl.csv", "Ligue 1": "playerstats_ligue1.csv",
                    "Bundesliga": "playerstats_bundesliga.csv", "Serie A": "playerstats_seriea.csv", "La Liga": "playerstats_laliga.csv"}
goalkeeper_file_dict = {"EPL": "goalkeeperstats_epl.csv", "Ligue 1": "goalkeeperstats_ligue1.csv",
                        "Bundesliga": "goalkeeperstats_bundesliga.csv", "Serie A": "goalkeeperstats_seriea.csv", "La Liga": "goalkeeperstats_laliga.csv"}

league = input(
    "Enter League Here (EPL, Ligue 1, Bundesliga, Serie A, La Liga). Press Enter when ready: ")

first_url_value = ""
league_code_value = ""
player_file_name = ""
goalkeeper_file_name = ""

if(url_dict.get(league) is None):
    print("Invalid League! Please enter League again!")
    exit()
else:
    first_url_value += url_dict[league]
    league_code_value += league_dict[league]
    player_file_name += player_file_dict[league]
    goalkeeper_file_name += goalkeeper_file_dict[league]

# Get List of Teams
url = 'https://fbref.com/en/comps/' + first_url_value
res = requests.get(url)
html_page = res.content

soup = BeautifulSoup(html_page, 'html.parser')

text_contains_squads = "/en/squads/"
teams_array = []
final_team_array = []
teams_exclude = ['/en/squads/', '/en/squads/411b1108/Arsenal-Women-Stats', '/en/squads/7f2012ad/Lyon-Women-Stats', '/en/squads/a1393014/Wolfsburg-Women-Stats', '/en/squads/613577b8/Juventus-Women-Stats', '/en/squads/795ca75e/Boca-Juniors-Stats', '/en/squads/2466c132/Sydney-FC-Stats', '/en/squads/6082332e/Melbourne-City-Women-Stats', '/en/squads/e69cb5b6/Bolivar-Stats', '/en/squads/639950ae/Flamengo-Stats', '/en/squads/488c6ba1/Ludogorets-Razgrad-Stats', '/en/squads/8514c671/Forge-FC-Stats', '/en/squads/3e3fbf36/Univ-Catolica-Stats', '/en/squads/1837b9f6/Guangzhou-Evergrande-Taobao-Stats', '/en/squads/e0b973a6/Atletico-Nacional-Stats', '/en/squads/111cbfb1/Slavia-Prague-Stats', '/en/squads/3c4fb635/Midtjylland-Stats', '/en/squads/d7319d80/HJK-Helsinki-Stats', '/en/squads/2fdb4aef/Olympiacos-Stats', '/en/squads/6611f992/Ferencvaros-Stats', '/en/squads/3249478a/Goa-Stats', '/en/squads/95f42e44/Persepolis-Stats', '/en/squads/858d58b2/Kawasaki-Frontale-Stats',
                 '/en/squads/ae23a242/Jeonbuk-Stats', '/en/squads/972e2539/Al-Hilal-Stats', '/en/squads/18d3c3a3/America-Stats', '/en/squads/174bd5a0/Molde-Stats', '/en/squads/ca6492f2/LSK-Kvinner-Stats', '/en/squads/4d4fc0b8/Olimpia-Asuncion-Stats', '/en/squads/8917b8a9/Sporting-Cristal-Stats', '/en/squads/a73408a7/Legia-Warsaw-Stats', '/en/squads/5e876ee6/Porto-Stats', '/en/squads/ff04e205/CFR-Cluj-Stats', '/en/squads/97d80fef/Mamelodi-Sundowns-Stats', '/en/squads/98ce363d/Zenit-Stats', '/en/squads/b81aa4fa/Celtic-Stats', '/en/squads/099c6eb5/Red-Star-Belgrade-Stats', '/en/squads/4b682260/Young-Boys-Stats', '/en/squads/f3d8c8b9/Malmo-Stats', '/en/squads/89f584e1/KopparbergsGoteborg-Stats', '/en/squads/0f9294bd/Besiktas-Stats', '/en/squads/e89d5a28/Shakhtar-Donetsk-Stats', '/en/squads/26ebba72/Nacional-Stats', '/en/squads/6218ebd4/Seattle-Sounders-FC-Stats', '/en/squads/85c458aa/North-Carolina-Courage-Stats', '/en/squads/2583cf18/Caracas-Stats']
text = soup.find_all("a", href=True)
for a in text:
    if text_contains_squads in a['href']:
        if a['href'] not in teams_exclude:
            teams_array.append(a['href'])

for i in teams_array:
    final_team_array.append("https://fbref.com"+i)

final_team_array = list(set(final_team_array))

for i in final_team_array:
  print(i)