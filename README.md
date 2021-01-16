# Fantasy Premier League Data Science

This project aims to predict the best determinants of scoring the maximum number of points for Fantasy Premier League, a fantasy soccer game where participants get to pick a list of players and are awarded points for each player picked based on the player's real life performance in soccer games.

This project consists of xxx number of steps.

## Step 1: Data Extraction from fbref (https://fbref.com/en/)

We extracted the data required for our analysis from the FBRef Website, which consists of a breakdown of a match-by-match performance for each player. File used to find this may be found here: https://github.com/hoyishian/fantasypldatascience/blob/main/fbref_extraction.py

There are 2 kind of players in the data we collected: Outfield players and Goalkeepers. 

### Goalkeeper Players
Goalkeeper players only have 1 set of statistics that is made up of 7 groups of Goalkeeping statistics:

#### Performance
SoTA -- Shots on Target Against

GA -- Goals Against

Save% -- Save Percentage (Shots on Target Against - Goals Against/Shots on Target Against)

CS -- Clean Sheets

Full matches by goalkeeper where no goals are allowed.

PSxG -- Post-Shot Expected Goals (PSxG is expected goals based on how likely the goalkeeper is to save the shot)

#### Penalty Kicks

PKatt -- Penalty Kicks Attempted

PKA -- Penalty Kicks Allowed

PKsv -- Penalty Kicks Saved

PKm -- Penalty Kicks Missed

#### Launched
Cmp -- Passes Completed

Passes longer than 40 yards

Att -- Passes Attempted

Passes longer than 40 yards

Cmp% -- Pass Completion Percentage

Passes longer than 40 yards

#### Passes
Att -- Passes Attempted (Not including goal kicks)

Thr -- Throws Attempted

Launch% -- Percentage of Passes that were Launched (Not including goal kicks)

Passes longer than 40 yards

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
Outfield players have 4 set of statistics:

#### Passing

#### Goal and Shot Creation

#### Defensive Actions

#### Possession

## Step 2:
