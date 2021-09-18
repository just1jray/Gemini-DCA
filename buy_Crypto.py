import json
import gemini
import secrets
import sys

# Designed to be used with iOS shorcuts app
# Use shortcuts to set variables for Symbol, Amount, and Tick Size
# Call script using ssh action
#   Usage:
#       python buy_Crypto.py symbol usd_amount tick_size

public_key = secrets.public_key
private_key = secrets.private_key
symbol = sys.argv[1] 
usd_amount = int(sys.argv[2])
tick_size = int(sys.argv[3])

def _buyCrypto(buy_size, pub_key, priv_key):
    trader = gemini.PrivateClient(pub_key, priv_key)
    factor = 0.999
    price = str(round(float(trader.get_ticker(symbol)['ask'])*factor,2))

    amount = round((buy_size*.999)/float(price), tick_size)

    buy = trader.new_order(symbol, str(amount), price, "buy", ["maker-or-cancel"])
    print(f'Maker Buy: {buy}')

def main():
    _buyCrypto(usd_amount, public_key, private_key)
    return {
            'statusCode': 200,
            'body': json.dumps('End of script')
            }

if __name__ == "__main__":
    main()
