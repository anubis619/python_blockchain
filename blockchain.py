blockchain = [[1]]


def getLastBlockchainValue():
    return blockchain[-1]


def addValue(transactionAmount):
    blockchain.append([getLastBlockchainValue(), transactionAmount])


addValue(2)
addValue(1232.212)
addValue(48323.131)

print(blockchain)
