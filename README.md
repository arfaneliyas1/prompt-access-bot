# Prompt Access Telegram Bot

## Description
A professional Telegram bot to access prompts and interact with users. Built with Python using `python-telegram-bot`. Features inline buttons for likes and surprise prompts.


## Features
- `/start` – Welcome message with guide  
- `/help` – Lists available commands  
- `/list` – Show all prompts with interactive buttons  
- `/latest` – Show the newest prompt  
- Inline buttons:
  - 👍 Like → Increment votes  
  - 🎲 Surprise Me → Shows a random prompt  


## File Structure

telegram_prompt_bot/
│
├── bot/
│   ├── main.py          # Entry point
│   ├── handlers.py      # Command & button handlers
│   └── utils.py         # Helper functions
│
├── data/
│   ├── prompts.json     # Dummy prompt data
│   └── votes.json       # Persistent vote storage
│
├── logs/
│   └── bot.log          # Generated logs
│
├── .env                 # Environment variables
├── requirements.txt     # Dependencies
└── README.md            # Documentation

## Notes

Prompts and votes are stored in local JSON files.

Inline buttons demonstrate minimal interactive functionality.