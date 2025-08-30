import logging
import os
from telegram.ext import Application
from .handlers import register_handlers
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()

    # -----------------------
    # Logging Configuration
    # -----------------------
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename="logs/bot.log",
        filemode="a"
    )
    logging.info("🚀 Starting Prompt Access Bot")

    # Get Telegram Bot Token
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    if not TOKEN:
        raise ValueError("❌ TELEGRAM_TOKEN not found in .env")

    # Initialize bot
    app = Application.builder().token(TOKEN).build()

    # Register all handlers
    register_handlers(app)

    logging.info("✅ Handlers registered successfully")
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
