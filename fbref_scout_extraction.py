import pandas as pd
import numpy as np
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
import sys
import time

def extract_goalkeeper_stats(player_link, goalkeeper_file_name):
    name = extractName(player_link)
    
    try:
        df = pd.read_html(player_link, header=1)[0]
        if (len(df.columns) < 36):
            print("Invalid length of columns", player_link)
            return
        df = df.drop(columns=['Match Report'])
        df = df.drop(columns=['Comp'], errors = 'ignore')
        df = df.rename(columns={"Day": "Name"})
        df.dropna(subset=["Date"], inplace=True)
        df['Name'] = df['Name'].replace(
                ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], name)
  
        if "PSxG" not in df.columns:
            df["Post-Shot Expected Goals"] = np.nan
        df = df.rename(columns={"Att": "PassAttemptedLong"})

        df = df.rename(columns={"Att.1": "PassAtt"})
        df = df.rename(columns={"Att.2": "GoalKickAtt"})
        df = df.rename(columns={"Launch%.1": "GKLaunch%"})
        df = df.rename(columns={"AvgLen.1": "GKAvgLen"})
        df.drop(
                    df[df["Pos"] == "On matchday squad, but did not play"].index, inplace=True)
        df = df[df.Round != "Round"]
        df['sort'] = df['Round'].str.extract(
                    '(\d+)', expand=False).astype(int)
        df.sort_values('sort', inplace=True)
        df = df.drop('sort', axis=1)
        df.fillna(0, inplace=True)

        if (len(df.columns) != 35):
            print("Invalid Number of Columns", player_link)
            return

        try:
            f = open(goalkeeper_file_name)
            df.to_csv(goalkeeper_file_name, index=False,
                        header=False, mode='a')
            f.close()
        except:
            df.to_csv(goalkeeper_file_name, index=False)
    except Exception:
        print(Exception)
        print("Invalid Goalkeeper", player_link)
        return


def extract_player_stats(player_link, player_file_name):
    name = extractName(player_link)
    new_player_link = player_link.replace("keeper", "passing")
    try:
        df = pd.read_html(new_player_link, header=1)[0]
        df = df.drop(columns=['Match Report'])
        df = df.drop(columns=['Comp'], errors = 'ignore')
        df = df.rename(columns={"Day": "Name"})
        df.dropna(subset=["Date"], inplace=True)
        df['Name'] = df['Name'].replace(
            ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], name)
        df = df.rename(columns={"Att": "PassAtt"})
        df = df.rename(
            columns={"TotDist": "PassTotDist"})
        df = df.rename(columns={"PrgDist": "PassPrgDist"})
        df = df.rename(columns={"1/3": "PassFinThird"})
        df = df.rename(columns={"Prog": "PassProg"})
        df.fillna(0, inplace=True)

        time.sleep(2)
        new_player_link = player_link.replace("keeper", "gca")
        df_2 = pd.read_html(new_player_link, header=1)[0]
        df_2 = df_2.drop(columns=['Match Report'])
        df_2 = df_2.drop(columns=['Comp'], errors = 'ignore')
        df_2 = df_2.rename(columns={"Day": "Name"})
        df_2.dropna(subset=["Date"], inplace=True)
        df_2['Name'] = df_2['Name'].replace(
            ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], name)
        df_2 = df_2.drop(['Date', 'Name', 'Round', 'Venue', 'Result',
                         'Squad', 'Opponent', 'Start', 'Pos', 'Min'], axis=1)
        df_2 = df_2.rename(
            columns={"PassLive": "PassLiveShot"})
        df_2 = df_2.rename(
            columns={"PassDead": "PassDeadShot"})
        df_2 = df_2.rename(
            columns={"Drib": "DribShot"})
        df_2 = df_2.rename(
            columns={"Sh": "ShLSh"})
        df_2 = df_2.rename(
            columns={"Def": "DefShot"})
        df_2 = df_2.rename(
            columns={"PassLive.1": "PassLiveGoal"})
        df_2 = df_2.rename(
            columns={"PassDead.1": "PassDeadGoal"})
        df_2 = df_2.rename(
            columns={"Drib.1": "DribGoal"})
        df_2 = df_2.rename(columns={"Sh.1": "ShGoal"})
        df_2 = df_2.rename(columns={"Fld.1": "FldGoal"})
        df_2 = df_2.rename(
            columns={"Def.1": "DefGoal"})
        df_2.fillna(0, inplace=True)

        time.sleep(1)
        new_player_link = player_link.replace("keeper", "defense")
        df_3 = pd.read_html(new_player_link, header=1)[0]
        df_3 = df_3.drop(columns=['Match Report'])
        df_3 = df_3.drop(columns=['Comp'], errors = 'ignore')
        df_3 = df_3.rename(columns={"Day": "Name"})
        df_3.dropna(subset=["Date"], inplace=True)
        df_3['Name'] = df_3['Name'].replace(
            ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], name)
        df_3 = df_3.drop(['Date', 'Name', 'Round', 'Venue', 'Result',
                         'Squad', 'Opponent', 'Start', 'Pos', 'Min'], axis=1)
        df_3 = df_3.rename(
            columns={"Def 3rd": "TacklesDef3rd"})
        df_3 = df_3.rename(
            columns={"Mid 3rd": "TacklesMid3rd"})
        df_3 = df_3.rename(columns={"Att 3rd": "TacklesAtt3rd"})
        df_3 = df_3.rename(columns={"Tkl.1": "DribTackled"})
        df_3 = df_3.rename(columns={"Att": "DribContest"})
        df_3 = df_3.rename(columns={"Tkl%": "DribTackled%"})
        df_3 = df_3.rename(columns={"Succ": "SuccPress"})
        df_3 = df_3.rename(columns={"%": "SuccPress%"})
        df_3 = df_3.rename(
            columns={"Def 3rd.1": "PressDef3rd"})
        df_3 = df_3.rename(
            columns={"Mid 3rd.1": "PressMid3rd"})
        df_3 = df_3.rename(
            columns={"Att 3rd.1": "PressAtt3rd"})
        df_3 = df_3.rename(
            columns={"Sh": "BlockSh"})
        df_3.fillna(0, inplace=True)

        time.sleep(3)
        new_player_link = player_link.replace("keeper", "possession")
        df_4 = pd.read_html(new_player_link, header=1)[0]
        df_4 = df_4.drop(columns=['Match Report'])
        df_4 = df_4.drop(columns=['Comp'], errors = 'ignore')
        df_4 = df_4.rename(columns={"Day": "Name"})
        df_4.dropna(subset=["Date"], inplace=True)
        df_4['Name'] = df_4['Name'].replace(
            ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], name)
        df_4 = df_4.drop(['Date', 'Name', 'Round', 'Venue', 'Result',
                         'Squad', 'Opponent', 'Start', 'Pos', 'Min'], axis=1)
        df_4 = df_4.rename(columns={"Def 3rd": "TouchDef3rd"})
        df_4 = df_4.rename(columns={"Mid 3rd": "TouchMid3rd"})
        df_4 = df_4.rename(columns={"Att 3rd": "TouchAtt3rd"})
        df_4 = df_4.rename(
            columns={"Att Pen": "AttPen"})
        df_4 = df_4.rename(columns={"Prog": "ProgCarries"})
        df_4 = df_4.rename(columns={"1/3": "CarriesFinThird"})
        df_4 = df_4.rename(columns={"Prog.1": "ProgPassRec"})
        df_4.fillna(0, inplace=True)

        time.sleep(2)
        new_player_link = player_link.replace("keeper", "summary")
        df_5 = pd.read_html(new_player_link, header=1)[0]
        df_5 = df_5.drop(columns=['Match Report'])
        df_5 = df_5.drop(columns=['Comp'], errors = 'ignore')
        df_5 = df_5.drop(columns=['Ast'], errors = 'ignore')
        df_5 = df_5.drop(columns=['Ast'], errors = 'ignore')
        df_5 = df_5.drop(columns=['Press'], errors = 'ignore')
        df_5 = df_5.drop(columns=['Tkl'], errors = 'ignore')
        df_5 = df_5.drop(columns=['Int'], errors = 'ignore')
        df_5 = df_5.drop(columns=['Blocks'], errors = 'ignore')
        df_5 = df_5.drop(columns=['xA'], errors = 'ignore')
        df_5 = df_5.drop(columns=['SCA'], errors = 'ignore')
        df_5 = df_5.drop(columns=['GCA'], errors = 'ignore')

        df_5 = df_5.drop(columns=['Cmp'], errors = 'ignore')
        df_5 = df_5.drop(columns=['Att'], errors = 'ignore')
        df_5 = df_5.drop(columns=['Cmp%'], errors = 'ignore')
        df_5 = df_5.drop(columns=['Prog'], errors = 'ignore')

        df_5 = df_5.drop(columns=['Carries'], errors = 'ignore')
        df_5 = df_5.drop(columns=['Prog.1'], errors = 'ignore')

        df_5 = df_5.drop(columns=['Succ'], errors = 'ignore')
        df_5 = df_5.drop(columns=['Att.1'], errors = 'ignore')

        df_5 = df_5.drop(columns=['Fls'], errors = 'ignore')
        df_5 = df_5.drop(columns=['Fld'], errors = 'ignore')
        df_5 = df_5.drop(columns=['Off'], errors = 'ignore')
        df_5 = df_5.drop(columns=['Crs'], errors = 'ignore')
        df_5 = df_5.drop(columns=['TklW'], errors = 'ignore')
        df_5 = df_5.drop(columns=['OG'], errors = 'ignore')
        df_5 = df_5.drop(columns=['PKwon'], errors = 'ignore')
        df_5 = df_5.drop(columns=['PKcon'], errors = 'ignore')
        df_5 = df_5.drop(columns=['Touches'], errors = 'ignore')

        df_5 = df_5.rename(columns={"Day": "Name"})
        df_5.dropna(subset=["Date"], inplace=True)
        df_5['Name'] = df_5['Name'].replace(
            ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], name)
        df_5 = df_5.drop(['Date', 'Name', 'Round', 'Venue', 'Result',
                         'Squad', 'Opponent', 'Start', 'Pos', 'Min'], axis=1)
        df_5.fillna(0, inplace=True)
            
        concatenated = pd.concat([df, df_2, df_3, df_4, df_5], axis=1)
        
        concatenated.drop(
            concatenated[concatenated["Date"] == "Date"].index, inplace=True)
        concatenated.drop(
                concatenated[concatenated["Pos"] == "On matchday squad, but did not play"].index, inplace=True)
        concatenated['sort'] = concatenated['Round'].str.extract(
                '(\d+)', expand=False).astype(int)
        concatenated.sort_values('sort', inplace=True)
        concatenated = concatenated.drop('sort', axis=1)
        if (len(concatenated.columns) != 101):
            print("Invalid Number of Columns", player_link)
            return
        try:
            f = open(player_file_name)
            concatenated.to_csv(
                player_file_name, index=False, header=False, mode='a')
            f.close()
        except:
            concatenated.to_csv(player_file_name, index=False)
    except Exception as e:
        print(e)
        print("Invalid Outfield Player", player_link)
        return


def extractName(player_link):
    # res = requests.get(player_link)
    # html_page = res.content
    res = Request(player_link, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'})
    html_page = urlopen(res).read()
    soup = BeautifulSoup(html_page, 'html.parser')
    # name = soup.find("h1", {"itemprop": "name"})
    name = soup.find("h1")
    return name.find("span").text

EPL_dict = {
    "Tottenham Hotspur": "https://fbref.com/en/squads/361ca564/Tottenham-Hotspur-Stats",
    "Everton": "https://fbref.com/en/squads/d3fd31cc/Everton-Stats",
    "Liverpool":"https://fbref.com/en/squads/822bd0ba/Liverpool-Stats",
    "Chelsea": "https://fbref.com/en/squads/cff3d9bb/Chelsea-Stats",
    "Crystal Palace": "https://fbref.com/en/squads/47c64c55/Crystal-Palace-Stats",
    "Manchester United": "https://fbref.com/en/squads/19538871/Manchester-United-Stats",
    "Leeds United": "https://fbref.com/en/squads/5bfb9659/Leeds-United-Stats",
    "Southampton" : "https://fbref.com/en/squads/33c895d4/Southampton-Stats",
    "Manchester City": "https://fbref.com/en/squads/b8fd03ef/Manchester-City-Stats",
    "West Ham":"https://fbref.com/en/squads/7c21e445/West-Ham-United-Stats",
    "Leicester City":"https://fbref.com/en/squads/a2d435b3/Leicester-City-Stats",
    "Wolves":"https://fbref.com/en/squads/8cec06e1/Wolverhampton-Wanderers-Stats",
    "Brighton":"https://fbref.com/en/squads/d07537b9/Brighton-and-Hove-Albion-Stats",
    "Arsenal":"https://fbref.com/en/squads/18bb7c10/Arsenal-Stats",
    "Brentford":"https://fbref.com/en/squads/cd051869/Brentford-Stats",
    "Burnley": "https://fbref.com/en/squads/943e8050/Burnley-Stats",
    "Norwich": "https://fbref.com/en/squads/1c781004/Norwich-City-Stats",
    "Watford":"https://fbref.com/en/squads/2abfe087/Watford-Stats",
    "Newcastle":"https://fbref.com/en/squads/b2b47a98/Newcastle-United-Stats",
    "Aston Villa":"https://fbref.com/en/squads/8602292d/Aston-Villa-Stats"
}

Bundesliga_dict = {
    "Mainz": "https://fbref.com/en/squads/a224b06a/Mainz-05-Stats",
    "Bayer Leverkusen": "https://fbref.com/en/squads/c7a9f859/Bayer-Leverkusen-Stats",
    "Arminia" : "https://fbref.com/en/squads/247c4b67/Arminia-Stats",
    "Freiburg" : "https://fbref.com/en/squads/a486e511/Freiburg-Stats",
    "Monchengladbach": "https://fbref.com/en/squads/32f3ee20/Monchengladbach-Stats",
    "Union Berlin": "https://fbref.com/en/squads/7a41008f/Union-Berlin-Stats",
    "Greuther Furth": "https://fbref.com/en/squads/12192a4c/Greuther-Furth-Stats",
    "RB Leipzig": "https://fbref.com/en/squads/acbb6a5b/RB-Leipzig-Stats",
    "Hertha BSC": "https://fbref.com/en/squads/2818f8bc/Hertha-BSC-Stats",
    "Wolfsburg":"https://fbref.com/en/squads/4eaa11d7/Wolfsburg-Stats",
    "Hoffenheim":"https://fbref.com/en/squads/033ea6b8/Hoffenheim-Stats",
    "Bayern Munich": "https://fbref.com/en/squads/054efa67/Bayern-Munich-Stats",
    "Koln":"https://fbref.com/en/squads/bc357bf7/Koln-Stats",
    "Dortmund": "https://fbref.com/en/squads/add600ae/Dortmund-Stats",
    "Stuttgart": "https://fbref.com/en/squads/598bc722/Stuttgart-Stats",
    "Eintracht Frankfurt": "https://fbref.com/en/squads/f0ac8ee6/Eintracht-Frankfurt-Stats",
    "Bochum" : "https://fbref.com/en/squads/b42c6323/Bochum-Stats",
    "Augsburg":"https://fbref.com/en/squads/0cdc4311/Augsburg-Stats"
}

Ligue1_dict = {
    "PSG":"https://fbref.com/en/squads/e2d8892c/Paris-Saint-Germain-Stats",
    "Nantes": "https://fbref.com/en/squads/d7a486cd/Nantes-Stats",
    "Nice":"https://fbref.com/en/squads/132ebc33/Nice-Stats",
    "Monaco":"https://fbref.com/en/squads/fd6114db/Monaco-Stats",
    "Brest":"https://fbref.com/en/squads/fb08dbb3/Brest-Stats",
    "Marseille":"https://fbref.com/en/squads/5725cc7b/Marseille-Stats",
    "Montpellier":"https://fbref.com/en/squads/281b0e73/Montpellier-Stats",
    "Lorient":"https://fbref.com/en/squads/d2c87802/Lorient-Stats",
    "Lille":"https://fbref.com/en/squads/cb188c0c/Lille-Stats",
    "Bordeaux":"https://fbref.com/en/squads/123f3efe/Bordeaux-Stats",
    "Lens": "https://fbref.com/en/squads/fd4e0f7d/Lens-Stats",
    "Strasbourg": "https://fbref.com/en/squads/c0d3eab4/Strasbourg-Stats",
    "Angers": "https://fbref.com/en/squads/69236f98/Angers-Stats",
    "Saint Etienne": "https://fbref.com/en/squads/d298ef2c/Saint-Etienne-Stats",
    "Metz": "https://fbref.com/en/squads/f83960ae/Metz-Stats",
    "Lyon:": "https://fbref.com/en/squads/d53c0b06/Lyon-Stats",
    "Rennes": "https://fbref.com/en/squads/b3072e00/Rennes-Stats",
    "Reims": "https://fbref.com/en/squads/7fdd64e0/Reims-Stats",
    "Clermont Foot": "https://fbref.com/en/squads/d9676424/Clermont-Foot-Stats",
    "Troyes": "https://fbref.com/en/squads/54195385/Troyes-Stats"
}

SerieA_dict = {
    "Udinese":"https://fbref.com/en/squads/04eea015/Udinese-Stats",
    "Milan": "https://fbref.com/en/squads/dc56fe14/Milan-Stats",
    "Cagliari":"https://fbref.com/en/squads/c4260e09/Cagliari-Stats",
    "Spezia":"https://fbref.com/en/squads/68449f6d/Spezia-Stats",
    "Sassuolo":"https://fbref.com/en/squads/e2befd26/Sassuolo-Stats",
    "Napoli":"https://fbref.com/en/squads/d48ad4ff/Napoli-Stats",
    "Atalanta":"https://fbref.com/en/squads/922493f3/Atalanta-Stats",
    "Empoli":"https://fbref.com/en/squads/a3d88bd8/Empoli-Stats",
    "Hellas Verona":"https://fbref.com/en/squads/0e72edf2/Hellas-Verona-Stats",
    "Sampdoria":"https://fbref.com/en/squads/8ff9e3b3/Sampdoria-Stats",
    "Juventus":"https://fbref.com/en/squads/e0652b02/Juventus-Stats",
    "Lazio":"https://fbref.com/en/squads/7213da33/Lazio-Stats",
    "Genoa":"https://fbref.com/en/squads/658bf2de/Genoa-Stats",
    "Roma":"https://fbref.com/en/squads/cf74a709/Roma-Stats",
    "Venezia":"https://fbref.com/en/squads/af5d5982/Venezia-Stats",
    "Fiorentina":"https://fbref.com/en/squads/421387cf/Fiorentina-Stats",
    "Salernitana":"https://fbref.com/en/squads/c5577084/Salernitana-Stats",
    "Torino":"https://fbref.com/en/squads/105360fe/Torino-Stats",
    "Internazionale":"https://fbref.com/en/squads/d609edc0/Internazionale-Stats",
    "Bologna":"https://fbref.com/en/squads/1d8099f8/Bologna-Stats"
}

LaLiga_dict = {
    "Sevilla":"https://fbref.com/en/squads/ad2be733/Sevilla-Stats",
    "Real Betis":"https://fbref.com/en/squads/fc536746/Real-Betis-Stats",
    "Rayo Vallecano":"https://fbref.com/en/squads/98e8af82/Rayo-Vallecano-Stats",
    "Granada":"https://fbref.com/en/squads/a0435291/Granada-Stats",
    "Mallorca":"https://fbref.com/en/squads/2aa12281/Mallorca-Stats",
    "Real Sociedad":"https://fbref.com/en/squads/e31d1cd9/Real-Sociedad-Stats",
    "Osasuna":"https://fbref.com/en/squads/03c57e2b/Osasuna-Stats",
    "Espanyol":"https://fbref.com/en/squads/a8661628/Espanyol-Stats",
    "Atletico Madrid":"https://fbref.com/en/squads/db3b9613/Atletico-Madrid-Stats",
    "Celta Vigo":"https://fbref.com/en/squads/f25da7fb/Celta-Vigo-Stats",
    "Real Madrid":"https://fbref.com/en/squads/53a2f082/Real-Madrid-Stats",
    "Barcelona":"https://fbref.com/en/squads/206d90db/Barcelona-Stats",
    "Cadiz":"https://fbref.com/en/squads/ee7c297c/Cadiz-Stats",
    "Athletic Club":"https://fbref.com/en/squads/2b390eca/Athletic-Club-Stats",
    "Valencia":"https://fbref.com/en/squads/dcc91a7b/Valencia-Stats",
    "Elche":"https://fbref.com/en/squads/6c8b07df/Elche-Stats",
    "Alaves":"https://fbref.com/en/squads/8d6fd021/Alaves-Stats",
    "Villarreal":"https://fbref.com/en/squads/2a8183b3/Villarreal-Stats",
    "Getafe":"https://fbref.com/en/squads/7848bd64/Getafe-Stats",
    "Levante":"https://fbref.com/en/squads/9800b6a1/Levante-Stats"
}

url_dict = {"EPL": "9/Premier-League-Stats", "Ligue 1": "13/Ligue-1-Stats",
                "Bundesliga": "20/Bundesliga-Stats", "Serie A": "11/Serie-A-Stats", "La Liga": "12/La-Liga-Stats"}
league_dict = {"EPL": "s11160", "Ligue 1": "s11183",
                "Bundesliga": "s11193", "Serie A": "s11222", "La Liga": "s11174"}
player_file_dict = {"EPL": "playerstats_epl.csv", "Ligue 1": "playerstats_ligue1.csv",
                        "Bundesliga": "playerstats_bundesliga.csv", "Serie A": "playerstats_seriea.csv", "La Liga": "playerstats_laliga.csv"}
similar_player_file_dict = {"EPL": "similar_player_epl.csv", "Ligue 1": "similar_player_ligue1.csv",
                        "Bundesliga": "similar_player_bundesliga.csv", "Serie A": "similar_player_seriea.csv", "La Liga": "similar_player_laliga.csv"}
goalkeeper_file_dict = {"EPL": "goalkeeperstats_epl.csv", "Ligue 1": "goalkeeperstats_ligue1.csv",
                            "Bundesliga": "goalkeeperstats_bundesliga.csv", "Serie A": "goalkeeperstats_seriea.csv", "La Liga": "goalkeeperstats_laliga.csv"}

def scrapeStats():
    

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

    final_team_array = []
    if (league == "EPL"):
        for teamurl in EPL_dict.items():
            final_team_array.append(teamurl[1])
    elif(league == "Ligue 1"):
        for teamurl in Ligue1_dict.items():
            final_team_array.append(teamurl[1])
    elif(league == "Bundesliga"):
        for teamurl in Bundesliga_dict.items():
            final_team_array.append(teamurl[1])

    elif(league == "Serie A"):
        for teamurl in SerieA_dict.items():
            final_team_array.append(teamurl[1])

    elif(league == "La Liga"):
        for teamurl in LaLiga_dict.items():
            final_team_array.append(teamurl[1])
    else:
        print("Invalid League! Please enter League again!")
        exit()

    # print(final_team_array)
    # Get List of all Players and their respective links

    player_array = []
    player_final_array = []
    final_link = []

    text_contains_players = "/en/players/"
    text_contains_summary = "summary"

    for team_url in final_team_array:
        # res = requests.get(team_url)
        # team_html_page = res.content
        res = Request(team_url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'})
        team_html_page = urlopen(res).read()

        soup_team = BeautifulSoup(team_html_page, 'html.parser')

        text = soup_team.find_all("a", href=True)
        for a in text:
            if text_contains_players in a["href"] and text_contains_summary in a["href"]:
                player_array.append(a["href"])
        player_array = list(set(player_array))

    for i in player_array:
        if "matchlog" in i:
            player_final_array.append("https://fbref.com"+i)

    # player_final_array = list(set(player_final_array))
    # for i in player_final_array:
    #     print(i)
    # print(player_final_array)
    for link in player_final_array:
        temp_link = link.replace("summary", "keeper")
        temp_link = temp_link.replace("2021-2022", league_code_value)
        final_link.append(temp_link)

    final_link = list(set(final_link))
    final_link.sort()

    # Check if Player is GK.
    # If GK, call extract_goalkeeper_stats
    # If not GK, call extract_player_stats
    for player in final_link:

        # res_player = requests.get(player)
        # html_page_player = res_player.content
        
        res = Request(player, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'})
        html_page_player = urlopen(res).read()

        new_soup = BeautifulSoup(html_page_player, 'html.parser')

        searched_word = "GK"

        new_result = new_soup.find_all(
            string=re.compile('.*{0}.*'.format(searched_word)))

        if(len(new_result) == 0):
            extract_player_stats(player, player_file_name)
        else:
            # print(player)
            extract_goalkeeper_stats(player, goalkeeper_file_name)
        time.sleep(10)

def scrapeSimilarPlayers():
    league = input(
        "Enter League Here (EPL, Ligue 1, Bundesliga, Serie A, La Liga). Press Enter when ready: ")

    first_url_value = ""
    league_code_value = ""
    player_file_name = ""
    goalkeeper_file_name = ""
    list_of_id = ["similar_GK", "similar_CB", "similar_FB", "similar_MF", "similar_FW", "similar_AM"]
    position = {"similar_GK": "GK", "similar_CB":"CB", "similar_FB":"FB", "similar_FW":"FW", "similar_AM":"AM", "similar_MF":"MF"}

    if(url_dict.get(league) is None):
        print("Invalid League! Please enter League again!")
        exit()
    else:
        first_url_value += url_dict[league]
        league_code_value += league_dict[league]
        player_file_name += player_file_dict[league]
        goalkeeper_file_name += goalkeeper_file_dict[league]

    # Get List of Teams

    final_team_array = []
    if (league == "EPL"):
        for teamurl in EPL_dict.items():
            final_team_array.append(teamurl[1])
    elif(league == "Ligue 1"):
        for teamurl in Ligue1_dict.items():
            final_team_array.append(teamurl[1])
    elif(league == "Bundesliga"):
        for teamurl in Bundesliga_dict.items():
            final_team_array.append(teamurl[1])

    elif(league == "Serie A"):
        for teamurl in SerieA_dict.items():
            final_team_array.append(teamurl[1])

    elif(league == "La Liga"):
        for teamurl in LaLiga_dict.items():
            final_team_array.append(teamurl[1])
    else:
        print("Invalid League! Please enter League again!")
        exit()
    
    player_array = []
    player_final_array = []

    text_contains_players = "/en/players/"
    text_contains_matchlogs = "matchlogs"

    for team_url in final_team_array:
        # res = requests.get(team_url)
        # team_html_page = res.content

        res = Request(team_url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'})
        team_html_page = urlopen(res).read()

        soup_team = BeautifulSoup(team_html_page, 'html.parser')

        text = soup_team.find_all("a", href=True)
        for a in text:
            if text_contains_players in a["href"] and text_contains_matchlogs not in a["href"]:
                player_array.append(a["href"])
        player_array = list(set(player_array))

    for i in player_array:
        player_final_array.append("https://fbref.com"+i)
    
    player_final_array.sort()
    player_final_array.remove("https://fbref.com/en/players/")
    for player in player_final_array:
        
        name_player = extractName(player)
        print(name_player)
        # res_player = requests.get(player)
        # html_page_player = res_player.content

        res = Request(player, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'})
        html_page_player = urlopen(res).read()
        new_soup = BeautifulSoup(html_page_player, 'html.parser')
        for id in list_of_id:
            list_of_similar_players = []
            name = new_soup.find("table", {"id": id})
            if (name is not None):
                tbody = name.find("tbody")
                all_td = tbody.find_all("td",{"data-stat":"player"})
                for td in all_td:
                    player_name = td.find("a").text
                    list_of_similar_players.append(player_name)
                    # print(list_of_similar_players)
                column_header = ["Name", "Position", "Rank 1","Rank 2", "Rank 3", "Rank 4", "Rank 5", "Rank 6", "Rank 7", "Rank 8", "Rank 9","Rank 10"]
                # print(position[id])
                list_of_similar_players.insert(0,position[id])
                list_of_similar_players.insert(0,name_player)
                final_data = pd.DataFrame(data = [list_of_similar_players], columns = column_header)
                player_file_name = similar_player_file_dict[league]
                try:
                    f = open(player_file_name)
                    final_data.to_csv(player_file_name, index=False, header=False, mode='a')
                    f.close()
                except:
                    final_data.to_csv(player_file_name, index=False)

scrapeStats()
# scrapeSimilarPlayers()