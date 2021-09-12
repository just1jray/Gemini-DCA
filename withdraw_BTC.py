import json
import gemini
import random
import secrets

public_key = secrets.public_key 
private_key = secrets.private_key
trader = gemini.PrivateClient(public_key, private_key)

#withdraws full available balance of specified coin to given address
def _withdrawFullCoinBalance(coin, address):
    amount = "0"
    for currency in trader.get_balance():
        if(currency['currency'] == coin):
            amount = currency['availableForWithdrawal']
            print(f'Amount Available for Withdrawal: {amount}')
    
    #Replace the amount variable below with ".001" to withdraw .001 BTC - change the amount if you want to withdraw some static amount
    withdraw = trader.withdraw_to_address(coin, address, amount)

def main():
    #Add btc_address below 
    #JUST MAKE SURE THAT YOUR WALLET ADDRESS IS THE SAME TOKEN AS THE WITHDRAWAL SYMBOL (ie. btc_address is a bitcoin address)
    bitcoin_withdrawal_symbol = "BTC"
    btc_address = secrets.btc_address
    _withdrawFullCoinBalance(bitcoin_withdrawal_symbol, btc_address)

    return {
        'statusCode': 200,
        'body': json.dumps('End of script')
    }

if __name__ == "__main__":
    main()
