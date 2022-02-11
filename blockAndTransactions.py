def getBlockInfo(rpcClient, blockInput):
    if (blockInput[0:2] != "00"): #if the input is block height
        blockNr = int(blockInput)
        blockHash = rpcClient.getblockhash(blockNr)
        block = rpcClient.getblock(blockHash)
        blockAdditionalInfo = rpcClient.getblockstats(blockNr)
    else: #if the input is block hash
        block = rpcClient.getblock(blockInput) 
        blockAdditionalInfo = rpcClient.getblockstats(blockInput)

    viewTransactionsInfo = input("Do you just want to see transactions in block? [y/<anything>] >>>")
    if (viewTransactionsInfo.upper() == "Y"): #if user wants to see just transactions in the block
        for i in block.items():
            if(i[0] == "tx"):
                print("List of transactions IDs: ")
                print("----------------------------------------------")
                for j in i[1]: #traversing through transaction id's based on tx, a bit silly variable names
                    print(str(j))
    else: #if user wants to see other relevant information in the block
        for i in block.items():
            if(i[0] != "tx"):
                print(i[0].capitalize() + " - " + str(i[1])) #print in order of Height - 12345 for example

        additionalInfoQuery = input("\nWould you like to see additional block information? [y/<anything>] >>> ")
        if(additionalInfoQuery.upper() == "Y"): #more additional information from second API
            print(f"\nTransaction volume - {blockAdditionalInfo['total_out']/100000000} BTC") # divided because initial value from API is in satoshi
            print(f"Total fee - {blockAdditionalInfo['totalfee']/100000000} BTC")
            print(f"Block reward - {blockAdditionalInfo['subsidy']/100000000} BTC")
            print(f"Average fee - {blockAdditionalInfo['avgfee']/100000000} BTC")
            print(f"Minimum fee - {blockAdditionalInfo['minfee']/100000000} BTC")
            print(f"Maximum fee - {blockAdditionalInfo['maxfee']/100000000} BTC")
            print(f"Number of inputs - {blockAdditionalInfo['ins']}")
            print(f"Number of outputs - {blockAdditionalInfo['outs']}")
   
    return


def getTransactionInformation(rpcClient, transactionHash):
    amountOut = 0 #inital output value is 0
    txRaw=rpcClient.getrawtransaction(transactionHash)
    txDetails = rpcClient.decoderawtransaction(txRaw)
    for i in txDetails.items():
        if(i[0] != "vout" and i[0] != "vin"): #ignored vout and vin because it makes everything unreadable, if there was a GUI I'd extract those as well
            print(i[0].capitalize() + " - " + str(i[1]))

    for i in txDetails["vout"]: #IZLAZI
        amountOut=amountOut+i["value"]
    print("Output value - " + str(amountOut) + " BTC")
    print("Inputs - " + str(len(txDetails["vin"])))
    print("Outputs - " + str(len(txDetails["vout"])))
    print("----------------------------------------------")
    print("Addresses, scripts and other data wasn't included because of unreadability in the terminal, in order to get that information please refer to some GUI block explorer")


def getCurrentBlock(rpcClient):
    print("Current block height is - " + str(rpcClient.getblockcount()))
    return

def getDifficulty(rpcClient):
    print("Current difficulty is - " + str(rpcClient.getdifficulty()))
    return

def getMempoolInfo(rpcClient):
    mempool = rpcClient.getmempoolinfo()
    for i in mempool.items():
        print(i[0].capitalize() + " - " + str(i[1]))
    return