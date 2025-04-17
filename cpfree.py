from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import logging
import requests  # Assuming your script uses requests

# Replace with your actual bot token
BOT_TOKEN = "8150437257:AAHYaDbgonl9VidabAHzGNavHrLcZcsi2Fk"

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Example logic you can customize
async def run_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    await update.message.reply_text(f"Running script for {user}...")

    try:
        # Your script's logic here instead of input/output
        response = requests.get("https://api.chucknorris.io/jokes/random")
        joke = response.json().get("value", "No joke found.")
        await update.message.reply_text(joke)
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

# Fallback for other messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send /run to start the script.")

# Main bot function
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("run", run_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    logger.info("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
