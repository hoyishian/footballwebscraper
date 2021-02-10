import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re

def extract_goalkeeper_stats(player_link, goalkeeper_file_name):
    name = extractName(player_link)
    # new_player_link = player_link.replace("summary", "keeper")
    # print(player_link)
    try:
        df = pd.read_html(player_link, header= 1)[0]
        df = df.drop(columns = ['Match Report'])
        df = df.rename(columns={"Day":"Name"})
        df.dropna(subset=["Date"], inplace =True)
        df['Name'] = df['Name'].replace(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], name)
        df = df.rename(columns={"SOT":"Shots on Target Against"})
        df = df.rename(columns={"GA":"Goals Against"})
        df = df.rename(columns={"Save%":"Save Percentage"})
        df = df.rename(columns={"CS":"Clean Sheets"})
        if "PSxG" not in df.columns:
            df["Post-Shot Expected Goals"] = np.nan
        else:
            df = df.rename(columns={"PSxG":"Post-Shot Expected Goals"})

        df = df.rename(columns={"PKatt":"Penalty Kicks Attempted"})
        df = df.rename(columns={"PKA":"Penalty Kicks Allowed"})
        df = df.rename(columns={"PKsv":"Penalty Kicks Saved"})
        df = df.rename(columns={"PKm":"Penalty Kicks Missed"})

        try:
            df.drop(df[df["Pos"] == "On matchday squad, but did not play"].index, inplace=True)
            df['sort'] = df['Round'].str.extract('(\d+)', expand=False).astype(int)
            df.sort_values('sort',inplace=True)
            df = df.drop('sort', axis=1)
            f = open(goalkeeper_file_name)
            df.to_csv(goalkeeper_file_name, index=False, header=False, mode = 'a')
            f.close()
        except:
            df["Passes Completed (Passes longer than 40 yards)"] = np.nan
            df["Passes Attempted (Passes longer than 40 yards)"] = np.nan
            df["Pass Completion Percentage (Passes longer than 40 yards)"] = np.nan
            df["Passes Attempted"] = np.nan
            df["Throws Attempted"] = np.nan
            df["Percentage of Passes that were Launched"] = np.nan
            df["Average length of passes, in yards"] = np.nan
            df["Goal Kick Passes Attempted"] = np.nan
            df["Percentage of Goal Kicks that were Launched"] = np.nan
            df["Average length of goal kicks"] = np.nan
            df["Opponent's attempted crosses into penalty area"] = np.nan
            df["Number of crosses into penalty area successfully stopped"] = np.nan
            df["Percentage of crosses into penalty area successfully stopped"] = np.nan
            df["Number of defensive actions outside of penalty area"] = np.nan
            df["Average distance from goal to perform defensive actions"] = np.nan
            df.drop(df[df["Pos"] == "On matchday squad, but did not play"].index, inplace=True)
            df['sort'] = df['Round'].str.extract('(\d+)', expand=False).astype(int)
            df.sort_values('sort',inplace=True)
            df = df.drop('sort', axis=1)
            df.to_csv(goalkeeper_file_name, index=False)
    except:
        print(player_link)
        return
def extract_player_stats(player_link, player_file_name):
    name = extractName(player_link)
    new_player_link = player_link.replace("keeper", "passing")
    try:
        df = pd.read_html(new_player_link, header= 1)[0]
        df = df.drop(columns = ['Match Report'])
        df = df.rename(columns={"Day":"Name"})
        df.dropna(subset=["Date"], inplace =True)
        df['Name'] = df['Name'].replace(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], name)
        df = df.rename(columns={"Cmp":"Total Passes Completed"})
        df = df.rename(columns={"Att":"Total Passes Attempted"})
        df = df.rename(columns={"Cmp%":"Total Pass Completion Percentage"})
        df = df.rename(columns={"TotDist":"Total Distance travelled by Passes"})
        df = df.rename(columns={"PrgDist":"Progressive Distance"})
        df = df.rename(columns={"Cmp.1":"Short Passes Completed"})
        df = df.rename(columns={"Att.1":"Short Passes Attempted"})
        df = df.rename(columns={"Cmp%.1":"Short Passes Completion Percentage"})
        df = df.rename(columns={"Cmp.2":"Medium Passes Completed"})
        df = df.rename(columns={"Att.2":"Medium Passes Attempted"})
        df = df.rename(columns={"Cmp%.2":"Medium Passes Completion Percentage"})
        df = df.rename(columns={"Cmp.3":"Long Passes Completed"})
        df = df.rename(columns={"Att.3":"Long Passes Attempted"})
        df = df.rename(columns={"Cmp%.3":"Long Passes Completion Percentage"})
        df = df.rename(columns={"Ast":"Assists"})
        df = df.rename(columns={"xA":"Expected Assist"})
        df = df.rename(columns={"KP":"Key Passes"})
        df = df.rename(columns={"1/3":"Passes into Final Third"})
        df = df.rename(columns={"PPA":"Passes into Penalty Area"})
        df = df.rename(columns={"CrsPA":"Crosses into Penalty Area"})
        df = df.rename(columns={"Prog":"Progressive Passes"})

        new_player_link = player_link.replace("keeper", "gca")
        df_2 = pd.read_html(new_player_link, header= 1)[0]
        df_2 = df_2.drop(columns = ['Match Report'])
        df_2 = df_2.rename(columns={"Day":"Name"})
        df_2.dropna(subset=["Date"], inplace =True)
        df_2['Name'] = df_2['Name'].replace(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], name)
        df_2 = df_2.drop(['Date', 'Name', 'Round', 'Venue','Result','Squad','Opponent','Start','Pos','Min'], axis = 1)
        df_2 = df_2.rename(columns={"SCA":"Shot-Creating Action"})
        df_2 = df_2.rename(columns={"PassLive":"Completed Live-Passes that lead to shot attempt"})
        df_2 = df_2.rename(columns={"PassDead":"Completed Dead-Passes that lead to shot attempt"})
        df_2 = df_2.rename(columns={"Drib":"Successful Dribbles that lead to shot attempt"})
        df_2 = df_2.rename(columns={"Sh":"Shot that lead to another shot attempt"})
        df_2 = df_2.rename(columns={"Fld":"Fouls drawn that lead to shot attempt"})
        df_2 = df_2.rename(columns={"Def":"Defensive Actions that lead to shot attempt"})
        df_2 = df_2.rename(columns={"GCA":"Goal-Creating Action"})
        df_2 = df_2.rename(columns={"PassLive.1":"Completed Live-Passes that lead to Goal"})
        df_2 = df_2.rename(columns={"PassDead.1":"Completed Dead-Passes that lead to Goal"})
        df_2 = df_2.rename(columns={"Drib.1":"Successful Dribbles that lead to Goal"})
        df_2 = df_2.rename(columns={"Sh.1":"Shot that lead to another Goal"})
        df_2 = df_2.rename(columns={"Fld.1":"Fouls drawn that lead to Goal"})
        df_2 = df_2.rename(columns={"Def.1":"Defensive Actions that lead to Goal"})
        df_2 = df_2.rename(columns={"OG":"Actions that lead to opponent scoring own goal"})

        
        new_player_link = player_link.replace("keeper", "defense")
        df_3 = pd.read_html(new_player_link, header= 1)[0]
        df_3 = df_3.drop(columns = ['Match Report'])
        df_3 = df_3.rename(columns={"Day":"Name"})
        df_3.dropna(subset=["Date"], inplace =True)
        df_3['Name'] = df_3['Name'].replace(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], name)
        df_3 = df_3.drop(['Date', 'Name', 'Round', 'Venue','Result','Squad','Opponent','Start','Pos','Min'], axis = 1)
        df_3 = df_3.rename(columns={"Tkl":"Number of players tackled"})
        df_3 = df_3.rename(columns={"TklW":"Tackles Won"})
        df_3 = df_3.rename(columns={"Def 3rd":"Tackles won in Defensive Third"})
        df_3 = df_3.rename(columns={"Mid 3rd":"Tackles won in Midfield Third"})
        df_3 = df_3.rename(columns={"Att 3rd":"Tackles won in Attack Third"})
        df_3 = df_3.rename(columns={"Tkl.1":"Number of Dribblers tackled"})
        df_3 = df_3.rename(columns={"Att":"Dribbles contested"})
        df_3 = df_3.rename(columns={"Tkl%":"Percentage of dribblers tackled"})
        df_3 = df_3.rename(columns={"Past":"Number of times dribbled past"})
        df_3 = df_3.rename(columns={"Press":"Pressures"})
        df_3 = df_3.rename(columns={"Succ":"Successful Pressures"})
        df_3 = df_3.rename(columns={"%":"Successful Pressure Percentage"})
        df_3 = df_3.rename(columns={"Def 3rd.1":"Number of times applying pressures in Defensive third"})
        df_3 = df_3.rename(columns={"Mid 3rd.1":"Number of times applying pressures in Midfield third"})
        df_3 = df_3.rename(columns={"Att 3rd.1":"Number of times applying pressures in Attacking third"})
        df_3 = df_3.rename(columns={"Blocks":"Number of times blocking the ball by standing in its path"})
        df_3 = df_3.rename(columns={"Sh":"Number of times blocking a shot by standing in its path"})
        df_3 = df_3.rename(columns={"ShSv":"Number of times blocking a shot that was on target, by standing in its path"})
        df_3 = df_3.rename(columns={"Pass":"Number of times blocking a pass by standing in its path"})
        df_3 = df_3.rename(columns={"Int":"Interceptions"})
        df_3 = df_3.rename(columns={"Tkl+Int":"Number of players tackled plus number of interceptions"})
        df_3 = df_3.rename(columns={"Clr":"Clearances"})
        df_3 = df_3.rename(columns={"Err":"Errors leading to an opponent's shot"})

        new_player_link = player_link.replace("keeper", "possession")
        df_4 = pd.read_html(new_player_link, header= 1)[0]
        df_4 = df_4.drop(columns = ['Match Report'])
        df_4 = df_4.rename(columns={"Day":"Name"})
        df_4.dropna(subset=["Date"], inplace =True)
        df_4['Name'] = df_4['Name'].replace(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], name)
        df_4 = df_4.drop(['Date', 'Name', 'Round', 'Venue','Result','Squad','Opponent','Start','Pos','Min'], axis = 1)
        df_4 = df_4.rename(columns={"Def Pen":"Touches in Defensive Penalty Area"})
        df_4 = df_4.rename(columns={"Def 3rd":"Touches in Defensive Third"})
        df_4 = df_4.rename(columns={"Mid 3rd":"Touches in Midfield Third"})
        df_4 = df_4.rename(columns={"Att 3rd":"Touches in Attacking Third"})
        df_4 = df_4.rename(columns={"Att Pen":"Touches in Attacking Penalty Area"})
        df_4 = df_4.rename(columns={"Live":"Live-Ball Touches"})
        df_4 = df_4.rename(columns={"Succ":"Dribbles completed successfully"})
        df_4 = df_4.rename(columns={"Att":"Dribbles attempted"})
        df_4 = df_4.rename(columns={"Succ%":"Percentage of Dribbles completed successfully"})
        df_4 = df_4.rename(columns={"#Pl":"Number of players dribbled past"})
        df_4 = df_4.rename(columns={"Megs":"Nutmegs"})
        df_4 = df_4.rename(columns={"TotDist":"Total Distance Carried"})
        df_4 = df_4.rename(columns={"PrgDist":"Progressive Distance"})
        df_4 = df_4.rename(columns={"Prog":"Progressive Carries"})
        df_4 = df_4.rename(columns={"1/3":"Carries into Final Third"})
        df_4 = df_4.rename(columns={"CPA":"Carries into Penalty Area"})
        df_4 = df_4.rename(columns={"Mis":"Miscontrols"})
        df_4 = df_4.rename(columns={"Dis":"Dispossessed"})
        df_4 = df_4.rename(columns={"Targ":"Pass Targets"})
        df_4 = df_4.rename(columns={"Rec":"Passes Received"})
        df_4 = df_4.rename(columns={"Rec%":"Passes Received Percentage"})

        concatenated = pd.concat([df, df_2, df_3, df_4], axis=1)
        concatenated.drop(concatenated[concatenated["Date"] == "Date"].index, inplace=True)
        try:
            concatenated.drop(concatenated[concatenated["Pos"] == "On matchday squad, but did not play"].index, inplace=True)
            concatenated['sort'] = concatenated['Round'].str.extract('(\d+)', expand=False).astype(int)
            concatenated.sort_values('sort',inplace=True)
            concatenated = concatenated.drop('sort', axis=1)
            f = open(player_file_name)
            concatenated.to_csv(player_file_name, index=False, header=False, mode = 'a')
            f.close()
        except:
            concatenated.drop(concatenated[concatenated["Pos"] == "On matchday squad, but did not play"].index, inplace=True)
            concatenated['sort'] = concatenated['Round'].str.extract('(\d+)', expand=False).astype(int)
            concatenated.sort_values('sort',inplace=True)
            concatenated = concatenated.drop('sort', axis=1)
            concatenated.to_csv(player_file_name, index=False)
    except:
        print(player_link)
        return

def extractName(player_link):
    res = requests.get(player_link)
    html_page = res.content

    soup = BeautifulSoup(html_page, 'html.parser')
    name = soup.find("h1", {"itemprop": "name"})
    print(name)
    return name.find("span").text



url_dict = {"EPL": "9/Premier-League-Stats", "Ligue 1": "13/Ligue-1-Stats", "Bundesliga": "20/Bundesliga-Stats", "Serie A": "11/Serie-A-Stats", "La Liga": "12/La-Liga-Stats"}
league_dict = {"EPL": "s10728", "Ligue 1": "s10732", "Bundesliga": "s10737", "Serie A": "s10730", "La Liga": "s10731"}
player_file_dict = {"EPL": "playerstats_epl.csv", "Ligue 1": "playerstats_ligue1.csv", "Bundesliga": "playerstats_bundesliga.csv", "Serie A": "playerstats_seriea.csv", "La Liga": "playerstats_laliga.csv"}
goalkeeper_file_dict = {"EPL": "goalkeeperstats_epl.csv", "Ligue 1": "goalkeeperstats_ligue1.csv", "Bundesliga": "goalkeeperstats_bundesliga.csv", "Serie A": "goalkeeperstats_seriea.csv", "La Liga": "goalkeeperstats_laliga.csv"}
    
league = input("Enter League Here (EPL, Ligue 1, Bundesliga, Serie A, La Liga). Press Enter when ready: ")

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
url = 'https://fbref.com/en/comps/'+ first_url_value
res = requests.get(url)
html_page = res.content

soup = BeautifulSoup(html_page, 'html.parser')

text_contains_squads = "/en/squads/"
teams_array = []
final_team_array = []
teams_exclude = ['/en/squads/', '/en/squads/411b1108/Arsenal-Women-Stats', '/en/squads/7f2012ad/Lyon-Women-Stats', '/en/squads/a1393014/Wolfsburg-Women-Stats', '/en/squads/613577b8/Juventus-Women-Stats', '/en/squads/795ca75e/Boca-Juniors-Stats', '/en/squads/2466c132/Sydney-FC-Stats', '/en/squads/6082332e/Melbourne-City-Women-Stats', '/en/squads/e69cb5b6/Bolivar-Stats', '/en/squads/639950ae/Flamengo-Stats', '/en/squads/488c6ba1/Ludogorets-Razgrad-Stats', '/en/squads/8514c671/Forge-FC-Stats', '/en/squads/3e3fbf36/Univ-Catolica-Stats', '/en/squads/1837b9f6/Guangzhou-Evergrande-Taobao-Stats', '/en/squads/e0b973a6/Atletico-Nacional-Stats', '/en/squads/111cbfb1/Slavia-Prague-Stats', '/en/squads/3c4fb635/Midtjylland-Stats', '/en/squads/d7319d80/HJK-Helsinki-Stats', '/en/squads/2fdb4aef/Olympiacos-Stats', '/en/squads/6611f992/Ferencvaros-Stats', '/en/squads/3249478a/Goa-Stats', '/en/squads/95f42e44/Persepolis-Stats', '/en/squads/858d58b2/Kawasaki-Frontale-Stats', '/en/squads/ae23a242/Jeonbuk-Stats', '/en/squads/972e2539/Al-Hilal-Stats', '/en/squads/18d3c3a3/America-Stats', '/en/squads/174bd5a0/Molde-Stats', '/en/squads/ca6492f2/LSK-Kvinner-Stats', '/en/squads/4d4fc0b8/Olimpia-Asuncion-Stats', '/en/squads/8917b8a9/Sporting-Cristal-Stats', '/en/squads/a73408a7/Legia-Warsaw-Stats', '/en/squads/5e876ee6/Porto-Stats', '/en/squads/ff04e205/CFR-Cluj-Stats', '/en/squads/97d80fef/Mamelodi-Sundowns-Stats', '/en/squads/98ce363d/Zenit-Stats', '/en/squads/b81aa4fa/Celtic-Stats', '/en/squads/099c6eb5/Red-Star-Belgrade-Stats', '/en/squads/4b682260/Young-Boys-Stats', '/en/squads/f3d8c8b9/Malmo-Stats', '/en/squads/89f584e1/KopparbergsGoteborg-Stats', '/en/squads/0f9294bd/Besiktas-Stats', '/en/squads/e89d5a28/Shakhtar-Donetsk-Stats', '/en/squads/26ebba72/Nacional-Stats', '/en/squads/6218ebd4/Seattle-Sounders-FC-Stats', '/en/squads/85c458aa/North-Carolina-Courage-Stats', '/en/squads/2583cf18/Caracas-Stats']
text = soup.find_all("a", href=True)
for a in text:
    if text_contains_squads in a['href']:
        if a['href'] not in teams_exclude:
            teams_array.append(a['href'])

for i in teams_array:
    final_team_array.append("https://fbref.com"+i)

final_team_array = list(set(final_team_array))
# print(final_team_array)
# Get List of all Premier League Players and their respective links
player_array = []
player_final_array = []
final_link = []

text_contains_players = "/en/players/"

for team_url in final_team_array:
    res = requests.get(team_url)
    team_html_page = res.content

    soup_team = BeautifulSoup(team_html_page, 'html.parser')
    
    text = soup_team.find_all("a", href=True)
    for a in text:
        if text_contains_players in a["href"]:
            player_array.append(a["href"])
    player_array = list(set(player_array))
# print(player_array)
for i in player_array:
    if "matchlog" in i:
        player_final_array.append("https://fbref.com"+i)

for link in player_final_array:
    temp_link = link.replace("summary", "keeper")
    temp_link = temp_link.replace("2020-2021", league_code_value)
    final_link.append(temp_link)

final_link = list(set(final_link))
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
        extract_player_stats(player, player_file_name)
    else:
        # print(player)
        extract_goalkeeper_stats(player, goalkeeper_file_name)