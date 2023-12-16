import json
import gemini
import mysecrets
import sys

#   Usage:
#       python buy_crypto.py usd_amount symbol [tick_size]
#
# Designed to be used with iOS shortcuts app or on remote server
# Tick size for symbols BTCUSD and ETHUSD set automatically, all others required
# Available symbols with tick size information can be found here: https://docs.gemini.com/rest-api/#symbols-and-minimums
# For shortcuts: set variables for USD Amount($), Symbol, and Tick Size

public_key = secrets.public_key
private_key = secrets.private_key

usd_amount = int(sys.argv[1])
symbol = sys.argv[2]

if symbol == "BTCUSD":
    tick_size = 8
elif symbol == "ETHUSD":
    tick_size = 6
else:
    tick_size = int(sys.argv[3])


def buy_crypto(buy_size, public_key, private_key):
    trader = gemini.PrivateClient(public_key, private_key)
    factor = 0.999
    price = str(round(float(trader.get_ticker(symbol)['ask']) * factor, 2))

    amount = round((buy_size * .998) / float(price), tick_size)

    buy = trader.new_order(symbol, str(amount), price, "buy", ["maker-or-cancel"])
    print(json.dumps(buy))


def main():
    buy_crypto(usd_amount, public_key, private_key)
    return {
        'statusCode': 200,
        'body': json.dumps('End of script')
    }


if __name__ == "__main__":
    main()
