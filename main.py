import loginRPC
from helpFunctions import getHelp, getBitcoinPrice
from blockAndTransactions import getBlockInfo, getTransactionInformation, getCurrentBlock, getDifficulty, getMempoolInfo    

def main():
    rpcClient = loginRPC.loginToRpc();

    while True:
        print("\nEnter 'help' if you want to se available commands")
        typeOfSearch = input("Which type of search do you want to make? >>> ")
        if typeOfSearch.upper() == "BLOCK":
            try:
                blockInput = input("Enter block height or block hash >>> ")
                getBlockInfo(rpcClient, blockInput)
            except:
                print("Invalid block, please try again!\n")
        elif typeOfSearch.upper() == "TRANSACTION":
            try:
                transactionHash = input("Please enter transaction hash you want to explore >>> ")
                getTransactionInformation(rpcClient,transactionHash)
            except:
                print("Invalid transaction ID!")
        elif typeOfSearch.upper() == "PRICE":
            getBitcoinPrice()
        elif typeOfSearch.upper() == "HELP":
            getHelp()
        elif typeOfSearch.upper() == "CURRENT":
            getCurrentBlock(rpcClient)
        elif typeOfSearch.upper() == "DIFFICULTY":
            getDifficulty(rpcClient)
        elif typeOfSearch.upper() == "MEMPOOL":
            getMempoolInfo(rpcClient)
        elif typeOfSearch.upper() == "EXIT" or typeOfSearch.upper() == "QUIT":
            print("----------------------------------------------")
            print("Goodbye!")
            print("----------------------------------------------")
            break
        else:
            print("Invalid input!\n")


if __name__ == "__main__" :
    main()