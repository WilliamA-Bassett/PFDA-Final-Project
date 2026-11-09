# Chainlinked

## Repository
https://github.com/WilliamA-Bassett/PFDA-Final-Project

## Description
Snake-like puzzle game where you play as a ball that collects chains to progress to the next level.

## Features
- Gameplay
  - The ball will move forward and can be turned around with the arrow keys, like Snake.
  - The goal of each level is to collect a chain to extend your chain tail.
- Levels
  - The game will consist of multiple levels with different layouts and obstacles.
  - With each level, your chain tail will be longer thanks to the chains you've collected, serving as its own obstacle.
- Losing
  - If the ball comes into contact with a level's walls or its own chain tail, you will die.
  - Dying restarts the level and loses you a life, lose all lives and you get a game over.

## Challenges
- Learn how to get a player sprite to move around on its own and turn around with player input.
- Learn how to make an extending tail of tiles that follows the player and grows every level.
- Learn how to make and store unique layouts for each and every level.
- Learn how to handle collision between the player and obstacles to cause the player to lose.

## Outcomes
Ideal outcome:
- A short, polished puzzle game, with around 20 or so levels that are well-tuned, as well as good sprite-work.

Minimal Viable Outcome:
- A short game that has at least the basic gameplay loop mentioned, a few levels, and basic images to display the player and obstacles.

## Milestones
- Week 1
  - Create a player character that moves around with player input.
  - Create a level goal for the player to reach (the chain) that moves the player to the next level.
  - Create a chain tail trailing effect on the player that grows with each level.
- Week 2
  - Finish chain tail trailing effect, if not done yet.
  - Get collision between player and chain tail working to result in a "death."
  - Create level loader and wall objects to make up basic layout of levels.
  - Create same collision for player and wall.
- Week 3
  - Finish any collision code, if not done yet.
  - Create each desired level within the level loader's data.
  - OPTIONAL: try to make some other unique gimmick or object to add to levels, like moving obstacles or speed tiles.
- Week 4 (Final)
  - Complete any basic gameplay stuff not yet finished.
  - If any additional optional content had been started on, try finishing it.
  - Add in sprite imagery to polish the game's looks, if time allots.
