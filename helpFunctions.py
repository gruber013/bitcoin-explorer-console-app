import requests

def getHelp(): #just print statements which should help user
        print("----------------------------------------------")
        print("Type 'block' if you want to explore blocks.") 
        print("Type 'transaction' if you want to explore transactions.")
        print("Type 'price' if you want to check current bitcoin value.")
        print("----------------------------------------------")
        print("Type 'current' to get the last mined block height.")
        print("Type 'difficulty' to get current block difficulty.")
        print("Type 'mempool' to view mempool info.")
        print("----------------------------------------------")
        print("Type 'exit' or 'quit' if you want to terminate the session.")

def getBitcoinPrice(): #used to get current bitcoin price in EUR,GBP or USD
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    price = response.json()
    try:
        currency = input("Do you want to use USD, GBP or EUR? >>> ")
        print("\nOn the " + price["time"]["updated"])
        print("1BTC is worth" + " " + price["bpi"][currency.upper()]["rate"] + currency.upper())
    except:
        print("Invalid currency!")