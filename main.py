from telegram import *
from telegram.ext import *
import requests
import json

bot = Bot("1766873339:AAGhxE5yTuoj0kGpr4dGq2W0CQieVZYY8gc")
print(bot.get_me())

updater = Updater("1766873339:AAGhxE5yTuoj0kGpr4dGq2W0CQieVZYY8gc", use_context=True)

dispatcher = updater.dispatcher

def getXRP(update:Update, context:CallbackContext):
    bot.send_message(chat_id=update.effective_chat.id, text="Fetching XRP/EUR value for Madeira NERDS")
    r = requests.get("https://api.kraken.com/0/public/Ticker?pair=XRPEUR")
    if r.status_code == requests.codes.ok:
        bot.send_message(chat_id=update.effective_chat.id, text=r.json()["result"]["XXRPZEUR"]["a"][0])
    else:
        bot.send_message(chat_id=update.effective_chat.id, text="I am having trouble fetching the data")

def getBTC(update:Update, context:CallbackContext):
    bot.send_message(chat_id=update.effective_chat.id, text="Fetching BTC/EUR value for Madeira NERDS")
    r = requests.get("https://api.kraken.com/0/public/Ticker?pair=BTCEUR")
    if r.status_code == requests.codes.ok:
        bot.send_message(chat_id=update.effective_chat.id, text=r.json()["result"]["XXBTZEUR"]["a"][0])
    else:
        bot.send_message(chat_id=update.effective_chat.id, text="I am having trouble fetching the data")

xrp = CommandHandler('XRP', getXRP)
btc = CommandHandler('BTC', getBTC)

dispatcher.add_handler(xrp)
dispatcher.add_handler(btc)

updater.start_polling()

