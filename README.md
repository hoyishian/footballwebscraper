# Fantasy Premier League Data Science

This project aims to predict the best determinants of scoring the maximum number of points for Fantasy Premier League, a fantasy soccer game where participants get to pick a list of players and are awarded points for each player picked based on the player's real life performance in soccer games.

This project consists of xxx number of steps.

## Step 1: Data Extraction from fbref (https://fbref.com/en/)

We extracted the data required for our analysis from the FBRef Website, which consists of a breakdown of a match-by-match performance for each player. File used to find this may be found here: https://github.com/hoyishian/fantasypldatascience/blob/main/fbref_extraction.py

There are 2 kind of players in the data we collected: Outfield players and Goalkeepers. 

### Goalkeeper Players
Goalkeeper players only have 1 set of statistics that is made up of 7 groups of Goalkeeping statistics. The following screenshot is taken from the FBRef website:

![Goalkeeping Screenshot from FBRef Website](/screenshots/Goalkeeping.png)

#### Performance
SoTA -- Shots on Target Against

GA -- Goals Against

Save% -- Save Percentage (Shots on Target Against - Goals Against/Shots on Target Against)

CS -- Clean Sheets (Full matches by goalkeeper where no goals are allowed.)

PSxG -- Post-Shot Expected Goals (PSxG is expected goals based on how likely the goalkeeper is to save the shot)

#### Penalty Kicks

PKatt -- Penalty Kicks Attempted

PKA -- Penalty Kicks Allowed

PKsv -- Penalty Kicks Saved

PKm -- Penalty Kicks Missed

#### Launched
Cmp -- Passes Completed (Passes longer than 40 yards)

Att -- Passes Attempted (Passes longer than 40 yards)

Cmp% -- Pass Completion Percentage (Passes longer than 40 yards)

#### Passes
Att -- Passes Attempted (Not including goal kicks)

Thr -- Throws Attempted

Launch% -- Percentage of Passes that were Launched (Not including goal kicks) (Passes longer than 40 yards)

AvgLen -- Average length of passes, in yards (Not including goal kicks)

#### Goal Kicks

Att -- Passes Attempted

Launch% -- Percentage of Goal Kicks that were Launched (Passes longer than 40 yards)

AvgLen -- Average length of goal kicks, in yards

#### Crosses

Opp -- Opponent's attempted crosses into penalty area

Stp -- Number of crosses into penalty area which were successfully stopped by the goalkeeper

Stp% -- Percentage of crosses into penalty area which were successfully stopped by the goalkeeper

#### Sweeper

#OPA -- # of defensive actions outside of penalty area

AvgDist -- Average distance from goal to perform defensive actions

### Outfield Players

Outfield players have 4 set of statistics. Screenshots are taken from the website:

#### Passing
![Passing Screenshot from FBRef Website](/screenshots/Passing.png)

##### Total

Cmp -- Passes Completed

Att -- Passes Attempted

Cmp% -- Pass Completion Percentage (Minimum 30 minutes played per squad game to qualify as a leader)

TotDist -- Total distance, in yards, that completed passes have traveled in any direction

PrgDist -- Progressive Distance (Total distance, in yards, that completed passes have traveled towards the opponent's goal. Note: Passes away from opponent's goal are counted as zero progressive yards.)

##### Short (Passes between 5 and 15 yards)
Cmp -- Passes Completed

Att -- Passes Attempted

Cmp% -- Pass Completion Percentage

##### Medium (Passes between 15 and 30 yards)
Cmp -- Passes Completed

Att -- Passes Attempted

Cmp% -- Pass Completion Percentage

##### Long (Passes longer than 30 yards)

Cmp -- Passes Completed

Att -- Passes Attempted

Cmp% -- Pass Completion Percentage

##### Performance
Ast -- Assists
xA -- xG Assisted (xG which follows a pass that assists a shot)

KP -- Key Passes (Passes that directly lead to a shot (assisted shots))

1/3 -- Passes into Final Third (Completed passes that enter the 1/3 of the pitch closest to the goal, Not including set pieces)

PPA -- Passes into Penalty Area (Completed passes into the 18-yard box, Not including set pieces)

CrsPA -- Crosses into Penalty Area (Completed crosses into the 18-yard box, Not including set pieces)

Prog -- Progressive Passes (Completed passes that move the ball towards the opponent's goal at least 10 yards from its furthest point in the last six passes, or any completed pass into the penalty area. Excludes passes from the defending 40% of the pitch)

#### Goal and Shot Creation
![GCA Screenshot from FBRef Website](/screenshots/GCA.png)

#### Defensive Actions
![Defensive Actions Screenshot from FBRef Website](/screenshots/DefensiveAction.png)

#### Possession
![Possession Screenshot from FBRef Website](/screenshots/Possession.png)

## Step 2:
