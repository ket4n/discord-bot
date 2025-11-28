# Discord Bot

A versatile Discord bot built in Python using discord.py, designed for both server management and fun interactions.

## Features

**Server Management**
- Giveaway system
- Role assignment system
- Moderation tools (kick, ban, mute)
- Ticket system for support

**Fun & Entertainment**
- Command-line chat games: Tic Tac Toe, Rock Paper Scissors
- Other interactive chat commands

**Utilities**
- Help command listing all available commands


## Run

- Clone the repo: 
```
git clone https://github.com/ket4n/discord-bot.git
```



- Navigate into the project folder:
```
cd discord-bot
```



- Create a virtual environment (Important: Don't skip this step, it's crucial to create a virtual environment to install these libraries as their versions are specified and they may get deprecated in future)
```
python -m venv venv
```



- Activate the Virtual Environment


1. For Windows:-
```
.\venv\Scripts\activate
```
2. For Linux:-
```
.\venv\bin\activate
```

- Install dependencies:
```
pip install -r requirements.txt
```



**Open the code and replace the bot token with your own in the appropriate place.**
- Run the bot (make sure the venv is activated before running this command):
```
python bot.py
```
The bot should now be online in your Discord server. Use the help command to see all available commands.
