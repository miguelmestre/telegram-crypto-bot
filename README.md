# telegram-crypto-bot
A simple telegram bot for crypto that uses Kraken Public API to fetch cryptocurrency prices.

If you like it you can buy me a coffee.

https://www.buymeacoffee.com/miguelmamfm

# Requirements
You need to have a valid Telegram Bot Key and add it to your environment variables.

Example:
```
BOT-KEY="17XXXXX39:AAGXXXXXXXXXXXXX0CQiXXXXgc"
```

# Install
```
pip install -r requirements.txt
```

# Run
```
python main.py
```

# Bot commands
## XRP/EUR pair

```
/xrp
```
Response:
```
0.97235000
```
## BTC/EUR pair
```
/btc
```
Response:
```
41460.90000
```
## Other Pairs
The cryptocurrencies must be comma separated 
```
/value DOGE,ETH,UNI
```
Response:
```
Value for DOGE is 0.243231100
Value for ETH is 2752.59000
Value for UNI is 22.77800
```
