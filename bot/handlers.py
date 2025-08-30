# Register all handlers
from telegram.ext import CommandHandler, CallbackQueryHandler

def register_handlers(app):
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("list", list_command))
    app.add_handler(CommandHandler("latest", latest_command))
    app.add_handler(CallbackQueryHandler(button_handler))
# bot/handlers.py
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from .import utils

logger = logging.getLogger(__name__)

# /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "👋 Hello, welcome to the *Prompt Access Bot*!\n\n"
        "I can help you explore prompts and interact with them.\n\n"
        "✨ Try these commands:\n"
        "/list – Show all prompts\n"
        "/latest – Show the newest prompt\n"
        "/help – List all commands\n\n"
        "Enjoy exploring! 🚀"
    )
    await update.message.reply_text(welcome_text, parse_mode="Markdown")

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "🤖 *Available Commands:*\n\n"
        "/help - Show this help message\n"
        "/list - List all prompts\n"
        "/latest - Show the newest prompt\n"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")


# /list command
async def list_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompts = utils.load_prompts()
    votes = utils.load_votes()

    if not prompts:
        await update.message.reply_text("⚠️ No prompts available.")
        return

    for prompt in prompts:
        count = votes.get(str(prompt["id"]), 0)
        keyboard = [
            [
                InlineKeyboardButton(f"👍 {count}", callback_data=f"like_{prompt['id']}"),
                InlineKeyboardButton("🎲 Surprise Me", callback_data="surprise"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(prompt["text"], reply_markup=reply_markup)


# /latest command
async def latest_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompts = utils.load_prompts()
    votes = utils.load_votes()

    if not prompts:
        await update.message.reply_text("⚠️ No prompts available.")
        return

    latest = prompts[-1]
    count = votes.get(str(latest["id"]), 0)
    keyboard = [
        [
            InlineKeyboardButton(f"👍 {count}", callback_data=f"like_{latest['id']}"),
            InlineKeyboardButton("🎲 Surprise Me", callback_data="surprise"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(latest["text"], reply_markup=reply_markup)


# Handle button callbacks
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data.startswith("like_"):
        prompt_id = data.split("_")[1]
        votes = utils.load_votes()
        votes[prompt_id] = votes.get(prompt_id, 0) + 1
        utils.save_votes(votes)

        count = votes[prompt_id]
        keyboard = [
            [
                InlineKeyboardButton(f"👍 {count}", callback_data=f"like_{prompt_id}"),
                InlineKeyboardButton("🎲 Surprise Me", callback_data="surprise"),
            ]
        ]
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "surprise":
        prompts = utils.load_prompts()
        if prompts:
            import random
            random_prompt = random.choice(prompts)
            votes = utils.load_votes()
            count = votes.get(str(random_prompt["id"]), 0)
            keyboard = [
                [
                    InlineKeyboardButton(f"👍 {count}", callback_data=f"like_{random_prompt['id']}"),
                    InlineKeyboardButton("🎲 Surprise Me", callback_data="surprise"),
                ]
            ]
            await query.message.reply_text(
                f"🎲 *Surprise Prompt:*\n{random_prompt['text']}",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
