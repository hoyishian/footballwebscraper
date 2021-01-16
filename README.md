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

##### SCA Types

SCA -- Shot-Creating Actions (The two offensive actions directly leading to a shot, such as passes, dribbles and drawing fouls. Note: A single player can receive credit for multiple actions and the shot-taker can also receive credit.)

PassLive -- Completed live-ball passes that lead to a shot attempt

PassDead -- Completed dead-ball passes that lead to a shot attempt. (Includes free kicks, corner kicks, kick offs, throw-ins and goal kicks)

Drib -- Successful dribbles that lead to a shot attempt

Sh -- Shots that lead to another shot attempt

Fld -- Fouls drawn that lead to a shot attempt

Def -- Defensive actions that lead to a shot attempt

##### GCA Types

GCA -- Goal-Creating Actions (The two offensive actions directly leading to a goal, such as passes, dribbles and drawing fouls. Note: A single player can receive credit for multiple actions and the shot-taker can also receive credit.)

PassLive -- Completed live-ball passes that lead to a goal

PassDead -- Completed dead-ball passes that lead to a goal. (Includes free kicks, corner kicks, kick offs, throw-ins and goal kicks)

Drib -- Successful dribbles that lead to a goal

Sh -- Shots that lead to another goal-scoring shot

Fld -- Fouls drawn that lead to a goal

Def -- Defensive actions that lead to a goal

OG -- Actions that led directly to an opponent scoring on their own goal


#### Defensive Actions
![Defensive Actions Screenshot from FBRef Website](/screenshots/DefensiveAction.png)

##### Tackles

Tkl -- Number of players tackled

TklW -- Tackles Won (Tackles in which the tackler's team won possession of the ball)

Def 3rd -- Tackles in defensive 1/3

Mid 3rd -- Tackles in middle 1/3

Att 3rd -- Tackles in attacking 1/3

##### Vs Dribbles

Tkl -- Number of dribblers tackled

Att -- Dribbles Contested (Number of times dribbled past plus number of tackles)

Tkl% -- Percentage of dribblers tackled (Dribblers tackled divided by dribblers tackled plus times dribbled past, Minimum .625 dribblers contested per squad game to qualify as a leader)

Past -- Number of times dribbled past by an opposing player

##### Pressures

Press -- Pressures (Number of times applying pressure to opposing player who is receiving, carrying or releasing the ball)

Succ -- Successful Pressures (Number of times the squad gained possession withing five seconds of applying pressure)

% -- Successful Pressure Percentage (Percentage of time the squad gained possession withing five seconds of applying pressure)

Def 3rd -- Number of times applying pressure to opposing player who is receiving, carrying or releasing the ball, in the defensive 1/3

Mid 3rd -- Number of times applying pressure to opposing player who is receiving, carrying or releasing the ball, in the middle 1/3

Att 3rd -- Number of times applying pressure to opposing player who is receiving, carrying or releasing the ball, in the attacking 1/3

##### Blocks

Blocks -- Number of times blocking the ball by standing in its path

Sh -- Number of times blocking a shot by standing in its path

ShSv -- Number of times blocking a shot that was on target, by standing in its path

Pass -- Number of times blocking a pass by standing in its path

Int -- Interceptions

Tkl+Int -- Number of players tackled plus number of interceptions

Clr -- Clearances

Err -- Errors (Mistakes leading to an opponent's shot)


#### Possession
![Possession Screenshot from FBRef Website](/screenshots/Possession.png)

##### Touches

Touches -- Number of times a player touched the ball. Note: Receiving a pass, then dribbling, then sending a pass counts as one touch

Def Pen -- Touches in defensive penalty area

Def 3rd -- Touches in defensive 1/3

Mid 3rd -- Touches in middle 1/3

Att 3rd -- Touches in attacking 1/3

Att Pen -- Touches in attacking penalty area

Live -- Live-ball touches. Does not include corner kicks, free kicks, throw-ins, kick-offs, goal kicks or penalty kicks

##### Dribbles
Succ -- Dribbles Completed Successfully

Att -- Dribbles Attempted

Succ% -- Percentage of Dribbles Completed Successfully

#Pl -- Number of Players Dribbled Past

Megs -- Nutmegs (Number of times a player dribbled the ball through an opposing player's legs)

##### Carries

Carries -- Number of times the player controlled the ball with their feet

TotDist -- Total distance, in yards, a player moved the ball while controlling it with their feet, in any direction

PrgDist -- Progressive Distance (Total distance, in yards, a player moved the ball while controlling it with their feet towards the opponent's goal)

Prog -- Progressive Carries (Carries that move the ball towards the opponent's goal at least 5 yards, or any carry into the penalty area. Excludes carries from the defending 40% of the pitch)

1/3 -- Carries into Final Third (Carries that enter the 1/3 of the pitch closest to the goal)

CPA -- Carries into Penalty Area (Carries into the 18-yard box)

Mis -- Miscontrols (Number of times a player failed when attempting to gain control of a ball)

Dis -- Dispossessed (Number of times a player loses control of the ball after being tackled by an opposing player. Does not include attempted dribbles)

##### Receiving
Targ -- Pass Targets (Number of times a player was the target of an attempted pass)

Rec -- Passes Received (Number of times a player successfully received a pass)

Rec% -- Passes Received Percentage (Percentage of time a player successfully received a pass)

## Step 2:
