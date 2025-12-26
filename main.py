import aiohttp
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "ТОКЕН_ОТ_BOTFATHER"

async def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,tether",
        "vs_currencies": "usd,rub"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            data = await response.json()

    return (
        "💰 КУРСЫ КРИПТО:\n\n"
        f"₿ BTC:\n"
        f"  💵 ${data['bitcoin']['usd']}\n"
        f"  🇷🇺 {data['bitcoin']['rub']} ₽\n\n"

        f"⧫ ETH:\n"
        f"  💵 ${data['ethereum']['usd']}\n"
        f"  🇷🇺 {data['ethereum']['rub']} ₽\n\n"

        f"💲 USDT:\n"
        f"  💵 ${data['tether']['usd']}\n"
        f"  🇷🇺 {data['tether']['rub']} ₽"
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Напиши /crypto чтобы узнать курсы криптовалют в USD и RUB."
    )

async def crypto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        prices = await get_crypto_prices()
        await update.message.reply_text(prices)
    except Exception:
        await update.message.reply_text("❌ Ошибка при получении курсов")

app = ApplicationBu
