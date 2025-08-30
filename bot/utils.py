import json
import os
import logging
from dotenv import load_dotenv

load_dotenv()

PROMPTS_FILE = os.getenv("PROMPTS_FILE", "data/prompts.json")
VOTES_FILE = os.getenv("VOTES_FILE", "data/votes.json")

# -----------------------
# Prompts
# -----------------------
def load_prompts():
    try:
        with open(PROMPTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            logging.info(f"Loaded {len(data)} prompts from {PROMPTS_FILE}")
            return data
    except Exception as e:
        logging.error(f"Failed to load prompts: {e}")
        return []

# -----------------------
# Votes
# -----------------------
def load_votes():
    if not os.path.exists(VOTES_FILE):
        return {}
    try:
        with open(VOTES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Failed to load votes: {e}")
        return {}

def save_votes(votes):
    try:
        with open(VOTES_FILE, "w", encoding="utf-8") as f:
            json.dump(votes, f, indent=2)
    except Exception as e:
        logging.error(f"Failed to save votes: {e}")
