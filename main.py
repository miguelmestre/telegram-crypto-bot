from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import os
from dotenv import load_dotenv


class CryptoBot:

    def __init__(self):
        load_dotenv()

        key=os.environ.get("BOT-KEY", None)
        self.bot = Bot(key)
        print(self.bot.get_me())

        self.updater = Updater(key, use_context=True)

        self.dispatcher = self.updater.dispatcher

        xrp = CommandHandler('XRP', self.getXRP)
        btc = CommandHandler('BTC', self.getBTC)
        value = CommandHandler(('VALUE'), self.getValue, pass_args=True)

        self.dispatcher.add_handler(xrp)
        self.dispatcher.add_handler(btc)
        self.dispatcher.add_handler(value)

    def getValue(self, update:Update, context:CallbackContext):
        for coin in context.args[0].split(','):
            pair = coin.upper() + "EUR"
            try:
                r = requests.get("https://api.kraken.com/0/public/Ticker?pair=" + pair)
                if r.status_code == requests.codes.ok:
                    # Key returned with the respponse for the pair
                    key = list(r.json()["result"].keys())[0]
                    text = "Value for " + coin.upper() + " is " + r.json()["result"][key]["a"][0] + " EUR"
                    self.bot.send_message(chat_id=update.effective_chat.id, text=text)
                else:
                    self.bot.send_message(chat_id=update.effective_chat.id, text="I am having trouble fetching the data for " + coin)
            except:
                self.bot.send_message(chat_id=update.effective_chat.id, text="I am having trouble fetching the data for " + coin)

    def getXRP(self, update:Update, context:CallbackContext):
        r = requests.get("https://api.kraken.com/0/public/Ticker?pair=XRPEUR")
        if r.status_code == requests.codes.ok:
            self.bot.send_message(chat_id=update.effective_chat.id, text=r.json()["result"]["XXRPZEUR"]["a"][0])
        else:
            self.bot.send_message(chat_id=update.effective_chat.id, text="I am having trouble fetching the data")

    def getBTC(self, update:Update, context:CallbackContext):
        r = requests.get("https://api.kraken.com/0/public/Ticker?pair=BTCEUR")
        print(r.status_code)
        if r.status_code == requests.codes.ok:
            self.bot.send_message(chat_id=update.effective_chat.id, text=r.json()["result"]["XXBTZEUR"]["a"][0])
        else:
            self.bot.send_message(chat_id=update.effective_chat.id, text="I am having trouble fetching the data")

    def run_bot(self):
        while True:
            self.updater.start_polling()
        return

CryptoBot().run_bot()
