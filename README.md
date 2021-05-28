# Football Data Science

This project aims to obtain the data available about a player's performance in their respective domestic leagues (e.g. English Premier League) and visualize their performance data in comparison to other players. We have broken up the analysis into 2 types of players in order to ensure a useful form of comparison.

This project consists of xxx number of steps.

## Step 1: Data Extraction from fbref (https://fbref.com/en/)

We extracted the data required for our analysis from the FBRef Website, which consists of a breakdown of a match-by-match performance for each player. File used to find this may be found here: https://github.com/hoyishian/fantasypldatascience/blob/main/fbref_scout_extraction.py

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

PassAttemptedLong -- Passes Attempted (Passes longer than 40 yards)

Cmp% -- Pass Completion Percentage (Passes longer than 40 yards)

#### Passes
PassAtt -- Passes Attempted (Not including goal kicks)

Thr -- Throws Attempted

Launch% -- Percentage of Passes that were Launched (Not including goal kicks) (Passes longer than 40 yards)

AvgLen -- Average length of passes, in yards (Not including goal kicks)

#### Goal Kicks

GoalKickAtt -- Passes Attempted

GKLaunch% -- Percentage of Goal Kicks that were Launched (Passes longer than 40 yards)

GKAvgLen -- Average length of goal kicks, in yards

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

PassAtt -- Passes Attempted

Cmp% -- Pass Completion Percentage (Minimum 30 minutes played per squad game to qualify as a leader)

PassTotDist -- Total distance, in yards, that completed passes have traveled in any direction

PassPrgDist -- Progressive Distance (Total distance, in yards, that completed passes have traveled towards the opponent's goal. Note: Passes away from opponent's goal are counted as zero progressive yards.)

##### Short (Passes between 5 and 15 yards)
Cmp.1 -- Passes Completed

Att.1 -- Passes Attempted

Cmp%.1 -- Pass Completion Percentage

##### Medium (Passes between 15 and 30 yards)
Cmp.2 -- Passes Completed

Att.2 -- Passes Attempted

Cmp%.2 -- Pass Completion Percentage

##### Long (Passes longer than 30 yards)

Cmp.3 -- Passes Completed

Att.3 -- Passes Attempted

Cmp%.3 -- Pass Completion Percentage

##### Performance
Ast -- Assists

xA -- xG Assisted (xG which follows a pass that assists a shot)

KP -- Key Passes (Passes that directly lead to a shot (assisted shots))

PassFinThird -- Passes into Final Third (Completed passes that enter the 1/3 of the pitch closest to the goal, Not including set pieces)

PPA -- Passes into Penalty Area (Completed passes into the 18-yard box, Not including set pieces)

CrsPA -- Crosses into Penalty Area (Completed crosses into the 18-yard box, Not including set pieces)

PassProg -- Progressive Passes (Completed passes that move the ball towards the opponent's goal at least 10 yards from its furthest point in the last six passes, or any completed pass into the penalty area. Excludes passes from the defending 40% of the pitch)

#### Goal and Shot Creation
![GCA Screenshot from FBRef Website](/screenshots/GCA.png)

##### SCA Types

SCA -- Shot-Creating Actions (The two offensive actions directly leading to a shot, such as passes, dribbles and drawing fouls. Note: A single player can receive credit for multiple actions and the shot-taker can also receive credit.)

PassLiveShot -- Completed live-ball passes that lead to a shot attempt

PassDeadShot -- Completed dead-ball passes that lead to a shot attempt. (Includes free kicks, corner kicks, kick offs, throw-ins and goal kicks)

DribShot -- Successful dribbles that lead to a shot attempt

ShLSh -- Shots that lead to another shot attempt

Fld -- Fouls drawn that lead to a shot attempt

DefShot -- Defensive actions that lead to a shot attempt

##### GCA Types

GCA -- Goal-Creating Actions (The two offensive actions directly leading to a goal, such as passes, dribbles and drawing fouls. Note: A single player can receive credit for multiple actions and the shot-taker can also receive credit.)

PassLiveGoal -- Completed live-ball passes that lead to a goal

PassDeadGoal -- Completed dead-ball passes that lead to a goal. (Includes free kicks, corner kicks, kick offs, throw-ins and goal kicks)

DribGoal -- Successful dribbles that lead to a goal

ShGoal -- Shots that lead to another goal-scoring shot

FldGoal -- Fouls drawn that lead to a goal

DefGoal -- Defensive actions that lead to a goal

OG -- Actions that led directly to an opponent scoring on their own goal


#### Defensive Actions
![Defensive Actions Screenshot from FBRef Website](/screenshots/DefensiveAction.png)

##### Tackles

Tkl -- Number of players tackled

TklW -- Tackles Won (Tackles in which the tackler's team won possession of the ball)

TacklesDef3rd -- Tackles in defensive 1/3

TacklesMid3rd -- Tackles in middle 1/3

TacklesAtt3rd -- Tackles in attacking 1/3

##### Vs Dribbles

DribTackled -- Number of dribblers tackled

DribContest -- Dribbles Contested (Number of times dribbled past plus number of tackles)

DribTackled% -- Percentage of dribblers tackled (Dribblers tackled divided by dribblers tackled plus times dribbled past, Minimum .625 dribblers contested per squad game to qualify as a leader)

Past -- Number of times dribbled past by an opposing player

##### Pressures

Press -- Pressures (Number of times applying pressure to opposing player who is receiving, carrying or releasing the ball)

SuccPress -- Successful Pressures (Number of times the squad gained possession withing five seconds of applying pressure)

SuccPress% -- Successful Pressure Percentage (Percentage of time the squad gained possession withing five seconds of applying pressure)

PressDef3rd -- Number of times applying pressure to opposing player who is receiving, carrying or releasing the ball, in the defensive 1/3

PressMid3rd -- Number of times applying pressure to opposing player who is receiving, carrying or releasing the ball, in the middle 1/3

PressAtt3rd -- Number of times applying pressure to opposing player who is receiving, carrying or releasing the ball, in the attacking 1/3

##### Blocks

Blocks -- Number of times blocking the ball by standing in its path

BlockSh -- Number of times blocking a shot by standing in its path

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

TouchDef3rd -- Touches in defensive 1/3

TouchMid3rd -- Touches in middle 1/3

TouchAtt3rd -- Touches in attacking 1/3

AttPen -- Touches in attacking penalty area

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

ProgCarries -- Progressive Carries (Carries that move the ball towards the opponent's goal at least 5 yards, or any carry into the penalty area. Excludes carries from the defending 40% of the pitch)

CarriesFinThird -- Carries into Final Third (Carries that enter the 1/3 of the pitch closest to the goal)

CPA -- Carries into Penalty Area (Carries into the 18-yard box)

Mis -- Miscontrols (Number of times a player failed when attempting to gain control of a ball)

Dis -- Dispossessed (Number of times a player loses control of the ball after being tackled by an opposing player. Does not include attempted dribbles)

##### Receiving
Targ -- Pass Targets (Number of times a player was the target of an attempted pass)

Rec -- Passes Received (Number of times a player successfully received a pass)

Rec% -- Passes Received Percentage (Percentage of time a player successfully received a pass)

#### Summary
![Summary Screenshot from FBRef Website](/screenshots/Summary.png)

ProgPassRec -- Completed passes that move the ball towards the opponent's goal at least 10 yards from its furthest point in the last six passes, or any completed pass into the penalty area. Excludes passes from the defending 40% of the pitch

Gls -- Goals

PK -- Penalty Kicks Made

PKatt -- Penalty Kicks Attempted

Sh -- Shots Total (Exclude PK)

SoT -- Shots on target (Exclude PK)

CrdY -- Yellow Cards

CrdR -- Red Cards

xG -- Expected Goals (xG totals include penalty kicks, but do not include penalty shootouts)

npxG -- Non-Penalty Expected Goals


## Step 2:
