# Initializing our blockchain list
blockchain = []


# Function definitions
def get_blockchain_value():
    """ Returns the last value of the current blockain. """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """Append a new value as well as the last blockchain value to the blockchain

    
    Arguments:
        :transaction_amount: => The amout that should be added
        :last_transaction: => The last blockchain value. Default ([1])
    """
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    """ Returns the input of the user (a new transaction amount) as a float. """
    return float(input("Please enter the amount of the transaction: "))


# Code execution where user inputs transaction value
tx_user_amount = get_user_input()
add_value(tx_user_amount)


tx_user_amount = get_user_input()
add_value(last_transaction=get_blockchain_value(),
         transaction_amount=tx_user_amount)


tx_user_amount = get_user_input()
add_value(tx_user_amount, get_blockchain_value())

# Result of the code.
print(blockchain)
