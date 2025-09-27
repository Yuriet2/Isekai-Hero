import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Bienvenido a Isekai-Hero! Usa /crear_heroe para empezar tu aventura.")

async def crear_heroe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Aquí se llamará al backend para registrar al héroe
    await update.message.reply_text("🎉 ¡Héroe creado! Pronto podrás personalizarlo.")

def get_bot_app():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("crear_heroe", crear_heroe))
    return app

async def start_bot():
    app = get_bot_app()
    await app.run_polling()