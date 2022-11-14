from web3 import Web3
from decouple import config


infuraUrl = config('INFURA_URL')
contractAddress = config('CONTRACT_ADDRESS')
ownerAddress = config('OWNER_ADDRESS')
privateKey = config('SUPER_SECRET_PRIVATE_KEY')
abi = '[{"inputs":[{"internalType":"string","name":"name_","type":"string"},{"internalType":"string","name":"symbol_","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'

web3 = Web3(Web3.HTTPProvider(infuraUrl))

def balanceOf(account):
    web3=Web3(Web3.HTTPProvider(infuraUrl))
    res=web3.isConnected()
    if res:
        contract_instance=web3.eth.contract(address=contractAddress,abi=abi)
        bal=contract_instance.functions.balanceOf(account).call()
    return bal

def decimals():
    web3=Web3(Web3.HTTPProvider(infuraUrl))
    res=web3.isConnected()
    if res:
        contract_instance=web3.eth.contract(address=contractAddress,abi=abi)
        decimals=contract_instance.functions.decimals().call()
    return decimals

def symbol():
    web3=Web3(Web3.HTTPProvider(infuraUrl))
    res=web3.isConnected()
    if res:
        contract_instance=web3.eth.contract(address=contractAddress,abi=abi)
        symbol=contract_instance.functions.symbol().call()
    return symbol

# check balance function works
print("Balance of my owner address in "+symbol()+ " is:"+str(balanceOf(ownerAddress)))

# check decimals works
print("Number of decimals in "+symbol()+" token is:"+str(decimals()))

# check Symbol works
print("Symbol of my token is: "+symbol())

res = web3.isConnected()

if res:
    print("Connected to Web3")

   