import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "ТОКЕН_ОТ_BOTFATHER"

def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,tether",
        "vs_currencies": "usd"
    }
    data = requests.get(url, params=params).json()
    return (
        f"💰 КУРСЫ КРИПТО:\n"
        f"BTC: ${data['bitcoin']['usd']}\n"
        f"ETH: ${data['ethereum']['usd']}\n"
        f"USDT: ${data['tether']['usd']}"
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Напиши /crypto чтобы узнать курсы криптовалют."
    )

async def crypto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prices = get_crypto_prices()
    await update.message.reply_text(prices)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("crypto", crypto))

print("Бот запущен...")
app.run_polling()
