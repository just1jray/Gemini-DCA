import json
import gemini
import secrets

public_key = secrets.public_key
private_key = secrets.private_key
symbol = "SUSHIUSD"
tick_size = 6 
usd_amount = 100
#update symbol based on what crypto/fiat pair you want to buy. Default is BTCUSD, change to BTCEUR for Euros or ETHUSD for Ethereum (for example) - see all possibilities down in symbols and minimums link
#update tick size based on what crypto-pair you are buying. BTC is 8. Check out the API link below to see what you need for your pair
#https://docs.gemini.com/rest-api/#symbols-and-minimums

def _buySushi(buy_size, pub_key, priv_key):
    trader = gemini.PrivateClient(pub_key, priv_key)
    factor = 0.999
    price = str(round(float(trader.get_ticker(symbol)['ask'])*factor,2))

    amount = round((buy_size*.998)/float(price), tick_size)

    buy = trader.new_order(symbol, str(amount), price, "buy", ["maker-or-cancel"])
    print(f'Maker Buy: {buy}')

def main():
    _buySushi(usd_amount, public_key, private_key)
    return {
            'statusCode': 200,
            'body': json.dumps('End of script')
            }

if __name__ == "__main__":
    main()
