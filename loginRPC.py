from bitcoinrpc.authproxy import AuthServiceProxy

def loginToRpc():
    rpcHost="" #I could've made this input value as well but it's defined here for simplicity
    rpcPort=""
    
    while True:
        try:
            rpcUsername = input("Enter your username >>> ")
            rpcPassword = input("Enter your password >>> ")
            rpcClient = AuthServiceProxy("http://"+rpcUsername+":"+rpcPassword+"@"+rpcHost+":"+rpcPort+"/")
            rpcClient.ping()
            return rpcClient
        except Exception: #if username or password is incorrect
            print("Invalid input, please try again!")

        except KeyboardInterrupt: #if user pressed Ctrl+C
            print("\nGoodbye!\n")
            quit()
