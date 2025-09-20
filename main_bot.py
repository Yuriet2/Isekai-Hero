from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import requests
import os

API_URL = "http://127.0.0.1:8000"  # FastAPI local
TOKEN = os.environ["BOT_TOKEN"]  # desde Replit Secrets

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Crear héroe", callback_data="create")],
        [InlineKeyboardButton("Ver héroe", callback_data="view")]
    ]
    await update.message.reply_text("Bienvenido al mundo Isekai RPG", 
                                    reply_markup=InlineKeyboardMarkup(keyboard))

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    if query.data == "create":
        res = requests.post(f"{API_URL}/create_hero/", params={"telegram_id": user_id})
        await query.edit_message_text(text=str(res.json()))

    elif query.data == "view":
        res = requests.get(f"{API_URL}/get_hero/{user_id}")
        await query.edit_message_text(text=str(res.json()))

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()

if __name__ == "__main__":
    main()
