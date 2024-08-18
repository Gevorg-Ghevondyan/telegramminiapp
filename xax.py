from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_TOKEN_HERE' with your bot's API token
TOKEN = "5980991673:AAG1GZwKgYn6AybukIT_HTwrpkzHSHc2CfM"  # Your actual bot token
GAME_URL = 'https://your-game-hosting-service.com/your-game'

def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    update.message.reply_text(f'Hi {user.first_name}! Use /play to start the game.')

def play(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Play the game here: {GAME_URL}')

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("play", play))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
