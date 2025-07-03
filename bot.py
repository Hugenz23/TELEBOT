from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import os

TOKEN = os.environ["TOKEN"]
LOOKER_URL = "https://lookerstudio.google.com/s/kEiifZOXtB0"
API_KEY = os.environ["API_KEY"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Ketik /scorecredit untuk ambil screenshot.")

async def scorecredit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Mengambil screenshot...")

    api_url = f"https://api.apiflash.com/v1/urltoimage?access_key={API_KEY}&url={LOOKER_URL}&full_page=true"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            with open("screenshot.png", "wb") as f:
                f.write(response.content)

            with open("screenshot.png", "rb") as photo:
                await update.message.reply_photo(photo)
        else:
            await update.message.reply_text(f"API gagal: {response.status_code}")
    except Exception as e:
        await update.message.reply_text(f"Terjadi error:\n{e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("scorecredit", scorecredit))
    app.run_polling()
