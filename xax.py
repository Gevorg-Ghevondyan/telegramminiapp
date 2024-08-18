from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackContext
import asyncio
import logging
import nest_asyncio

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

# Replace 'YOUR_BOT_API_TOKEN' with your actual bot token
TOKEN = "5980991673:AAG1GZwKgYn6AybukIT_HTwrpkzHSHc2CfM"  # Your actual bot token

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Start command handler
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Play Tapping Game", web_app=dict(url='https://gevorg-ghevondyan.github.io/telegramminiapp/'))]  # Replace with your web app URL
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Welcome! Click the button below to play the tapping game.', reply_markup=reply_markup)

# Main function
async def main():
    logging.info("Starting bot...")
    application = Application.builder().token(TOKEN).build()
    logging.info("Application built.")
    
    application.add_handler(CommandHandler("start", start))
    logging.info("Handler added.")
    
    # Run the bot
    await application.run_polling()

# Ensure we are not in an interactive environment
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except RuntimeError as e:
        logging.error(f"RuntimeError: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
