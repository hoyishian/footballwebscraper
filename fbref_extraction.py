import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

def extract_goalkeeper_stats(player_link):
    new_player_link = player_link.replace("summary", "keeper")
    df = pd.read_html(new_player_link)[0]
    print(df)

def extract_player_stats(player_link):
    new_player_link = player_link.replace("summary", "passing")
    df = pd.read_html(new_player_link)[0]
    print(df)
    

# Get List of Premier League Teams
url = 'https://fbref.com/en/comps/9/stats/Premier-League-Stats'
res = requests.get(url)
html_page = res.content

soup = BeautifulSoup(html_page, 'html.parser')

text_contains_squads = "/en/squads/"
teams_array = []
final_team_array = []
teams_exclude = ['/en/squads/', '/en/squads/822bd0ba/Liverpool-Stats', '/en/squads/411b1108/Arsenal-Women-Stats', '/en/squads/206d90db/Barcelona-Stats', '/en/squads/e2d8892c/Paris-Saint-Germain-Stats', '/en/squads/7f2012ad/Lyon-Women-Stats', '/en/squads/054efa67/Bayern-Munich-Stats', '/en/squads/a1393014/Wolfsburg-Women-Stats', '/en/squads/e0652b02/Juventus-Stats', '/en/squads/613577b8/Juventus-Women-Stats', '/en/squads/795ca75e/Boca-Juniors-Stats', '/en/squads/2466c132/Sydney-FC-Stats', '/en/squads/6082332e/Melbourne-City-Women-Stats', '/en/squads/50f2a074/Red-Bull-Salzburg-Stats', '/en/squads/f1e6c5f1/Club-Brugge-Stats', '/en/squads/e69cb5b6/Bolivar-Stats', '/en/squads/639950ae/Flamengo-Stats', '/en/squads/488c6ba1/Ludogorets-Razgrad-Stats', '/en/squads/8514c671/Forge-FC-Stats', '/en/squads/3e3fbf36/Univ-Catolica-Stats', '/en/squads/1837b9f6/Guangzhou-Evergrande-Taobao-Stats', '/en/squads/e0b973a6/Atletico-Nacional-Stats', '/en/squads/edd0d381/Dinamo-Zagreb-Stats', '/en/squads/111cbfb1/Slavia-Prague-Stats', '/en/squads/3c4fb635/Midtjylland-Stats', '/en/squads/8c71aef1/Barcelona-SC-Stats', '/en/squads/d7319d80/HJK-Helsinki-Stats', '/en/squads/2fdb4aef/Olympiacos-Stats', '/en/squads/6611f992/Ferencvaros-Stats', '/en/squads/3249478a/Goa-Stats', '/en/squads/95f42e44/Persepolis-Stats', '/en/squads/858d58b2/Kawasaki-Frontale-Stats', '/en/squads/ae23a242/Jeonbuk-Stats', '/en/squads/972e2539/Al-Hilal-Stats', '/en/squads/18d3c3a3/America-Stats', '/en/squads/19c3f8c4/Ajax-Stats', '/en/squads/9522e7b4/PSV-Stats', '/en/squads/174bd5a0/Molde-Stats', '/en/squads/ca6492f2/LSK-Kvinner-Stats', '/en/squads/4d4fc0b8/Olimpia-Asuncion-Stats', '/en/squads/8917b8a9/Sporting-Cristal-Stats', '/en/squads/a73408a7/Legia-Warsaw-Stats', '/en/squads/5e876ee6/Porto-Stats', '/en/squads/ff04e205/CFR-Cluj-Stats', '/en/squads/97d80fef/Mamelodi-Sundowns-Stats', '/en/squads/98ce363d/Zenit-Stats', '/en/squads/b81aa4fa/Celtic-Stats', '/en/squads/099c6eb5/Red-Star-Belgrade-Stats', '/en/squads/4b682260/Young-Boys-Stats', '/en/squads/f3d8c8b9/Malmo-Stats', '/en/squads/89f584e1/KopparbergsGoteborg-Stats', '/en/squads/0f9294bd/Besiktas-Stats', '/en/squads/e89d5a28/Shakhtar-Donetsk-Stats', '/en/squads/26ebba72/Nacional-Stats', '/en/squads/6218ebd4/Seattle-Sounders-FC-Stats', '/en/squads/85c458aa/North-Carolina-Courage-Stats', '/en/squads/2583cf18/Caracas-Stats']
text = soup.find_all("a", href=True)
for a in text:
    if text_contains_squads in a['href']:
        if a['href'] not in teams_exclude:
            teams_array.append(a['href'])

for i in teams_array:
    final_team_array.append("https://fbref.com"+i)

# Get List of all Premier League Players and their respective links
player_array = []
player_final_array = []
final_link = []

text_contains_players = "/en/players/"

players_to_remove = ['/en/players/', '/en/players/5b97f5ec/Yuki-Nagasato', '/en/players/b5b0068e/Onome-Ebi', '/en/players/e2e9c250/Santi-Cazorla', '/en/players/293211e1/Aritz-Aduriz', '/en/players/b418dbd4/Raul-Garcia', '/en/players/71c5f16f/Andrea-Pirlo', '/en/players/cda50d6b/Mana-Iwabuchi', '/en/players/f07be45a/Wayne-Rooney', '/en/players/82dbf623/Fernando-Llorente', '/en/players/ee65d412/Precious-Dede', '/en/players/e342ad68/Mohamed-Salah', '/en/players/e358587b/Pepe-Reina', '/en/players/655e7bd0/Alexandra-Popp', '/en/players/63b0ca6b/Alvaro-Negredo', '/en/players/59ef6268/Tobin-Heath']


for team_url in final_team_array:
    res = requests.get(team_url)
    team_html_page = res.content

    soup_team = BeautifulSoup(team_html_page, 'html.parser')
    
    text = soup_team.find_all("a", href=True)
    for a in text:
        if text_contains_players in a["href"]:
            if a["href"] not in players_to_remove:
                player_array.append(a["href"])
    player_array = list(set(player_array))

for i in player_array:
    if "matchlog" in i:
        player_final_array.append("https://fbref.com"+i)

for link in player_final_array:
    final_link.append(link.replace("2020-2021", "s10728"))

final_link.sort()

# Check if Player is GK. 
# If GK, call extract_goalkeeper_stats
# If not GK, call extract_player_stats
for player in final_link:

    res_player = requests.get(player)
    html_page_player = res_player.content

    new_soup = BeautifulSoup(html_page_player, 'html.parser')

    searched_word = "GK"

    new_result = new_soup.find_all(string= re.compile('.*{0}.*'.format(searched_word)))

    if(len(new_result) == 0):
        extract_player_stats(player)
    else:
        extract_goalkeeper_stats(player)
    break