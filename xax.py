import asyncio
import nest_asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update  # type: ignore
from telegram.ext import Application, CommandHandler, CallbackQueryHandler  # type: ignore

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

# Replace 'YOUR_BOT_API_TOKEN_HERE' with your actual bot token
TOKEN = "5980991673:AAG1GZwKgYn6AybukIT_HTwrpkzHSHc2CfM"

# Game state
game_state = {
    'coins': 0,
    'buildings': []
}

# Start command handler
async def start(update: Update, context):
    await update.message.reply_text("Welcome to City Tap Tycoon! Start tapping to earn coins.")
    await show_main_menu(update, context)

# Show the main menu
async def show_main_menu(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Tap", callback_data='tap')],
        [InlineKeyboardButton("Build", callback_data='build')],
        [InlineKeyboardButton("City", callback_data='city')],
        [InlineKeyboardButton("Mini App", callback_data='mini_app')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Main Menu:', reply_markup=reply_markup)

# Handle tapping
async def tap(update: Update, context):
    query = update.callback_query
    game_state['coins'] += 1
    await query.edit_message_text(f"You tapped! Coins: {game_state['coins']}")
    await show_main_menu(update, context)

# Handle building menu
async def build(update: Update, context):
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("House (10 coins)", callback_data='build_house')],
        [InlineKeyboardButton("Factory (20 coins)", callback_data='build_factory')],
        [InlineKeyboardButton("Back", callback_data='back')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text('Choose a building:', reply_markup=reply_markup)

# Handle building selection
async def handle_building(update: Update, context):
    query = update.callback_query
    if query.data == 'build_house' and game_state['coins'] >= 10:
        game_state['coins'] -= 10
        game_state['buildings'].append('House')
        await query.edit_message_text(f"House built! Coins: {game_state['coins']}")
    elif query.data == 'build_factory' and game_state['coins'] >= 20:
        game_state['coins'] -= 20
        game_state['buildings'].append('Factory')
        await query.edit_message_text(f"Factory built! Coins: {game_state['coins']}")
    else:
        await query.edit_message_text("Not enough coins!")
    await show_main_menu(update, context)

# Show the city status
async def show_city(update: Update, context):
    query = update.callback_query
    buildings = '\n'.join(game_state['buildings']) or "No buildings yet."
    await query.edit_message_text(f"Your city:\n{buildings}")
    await show_main_menu(update, context)

# Mini app feature
async def mini_app(update: Update, context):
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("Feature 1", callback_data='feature_1')],
        [InlineKeyboardButton("Feature 2", callback_data='feature_2')],
        [InlineKeyboardButton("Back", callback_data='back')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text('Mini App Menu:', reply_markup=reply_markup)

# Handle mini app features
async def handle_mini_app_features(update: Update, context):
    query = update.callback_query
    if query.data == 'feature_1':
        await query.edit_message_text("Feature 1 activated!")
    elif query.data == 'feature_2':
        await query.edit_message_text("Feature 2 activated!")
    else:
        await query.edit_message_text("Unknown feature!")
    await mini_app(update, context)

# Back to main menu
async def go_back(update: Update, context):
    query = update.callback_query
    await show_main_menu(update, context)

# Main function
async def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(tap, pattern='tap'))
    application.add_handler(CallbackQueryHandler(build, pattern='build'))
    application.add_handler(CallbackQueryHandler(handle_building, pattern='build_'))
    application.add_handler(CallbackQueryHandler(show_city, pattern='city'))
    application.add_handler(CallbackQueryHandler(mini_app, pattern='mini_app'))
    application.add_handler(CallbackQueryHandler(handle_mini_app_features, pattern='feature_'))
    application.add_handler(CallbackQueryHandler(go_back, pattern='back'))

    # Run the bot
    await application.run_polling()

if __name__ == '__main__':
    # Create and run the event loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
