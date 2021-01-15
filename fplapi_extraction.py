# import pandas as pd
import requests
import json
# url = 'https://fbref.com/en/players/e342ad68/matchlogs/2020-2021/summary/Mohamed-Salah-Match-Logs'
#
# df_list = pd.read_html(url)
#
# print(df_list)
team_dictionary = {1: 'Arsenal', 2: 'Aston Villa', 3: 'Brighton', 4: 'Burnley', 5: 'Chelsea', 6: 'Crystal Palace', 7: 'Everton', 8: 'Fulham', 9: 'Leicester City', 10: 'Leeds United', 11: 'Liverpool', 12: 'Manchester City', 13:'Manchester United', 14: 'Newcastle United', 15: 'Sheffield United', 16: 'Southampton', 17: 'Tottenham Hotspurs', 18: 'West Bromwich Albion', 19: 'West Ham', 20: 'Wolverhampton Wanderers'}
def define_team(id):
    return team_dictionary[id]


class Player:
    def __init__(self, id, webname, team, influence, creativity, threat, ict):
        self.id = id
        self.webname = webname
        self.team = team
        self.influence = influence
        self.creativity = creativity
        self.threat = threat
        self.ict = ict

players = []
r = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
json_object = r.json()
for player in json_object["elements"]:
    new_player = Player(player["id"], player["web_name"], define_team(player["team"]), player["influence"], player["creativity"], player["threat"], player["ict_index"])
    players.append(new_player)

player_name = input()
for player in players:
    if (player.webname.lower() == player_name):
        print("Name: ", player.webname)
        print("Team: ", player.team)
        print("Influence: ", player.influence)
        print("Creativity: ", player.creativity)
        print("Threat: ", player.threat)
        print("ICT: ", player.ict)