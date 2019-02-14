# Initializing our blockchain list
genesis_block = {'previous_hash': '', 'index': 0, 'transactions': []}
blockchain = [genesis_block]
open_transactions=[]
owner = "Alex"

def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


# Function definitions
def get_blockchain_value():
    """ Returns the last value of the current blockain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender = owner, amount=1.0):
    """Append a new value as well as the last blockchain value to the blockchain


    Arguments:
        :sender: The sender of the coins
        :recipinet: The recipient of the coins
        :amount: The amount of coins sent with the transaction.(Default of 1)
    """
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transactions.append(transaction)
    

def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions:': open_transactions
    }
    blockchain.append(block)


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    tx_recipient = input("Enter the recipinet of the transaction: ")
    tx_amount = float(input("Please enter the amount of the transaction: "))
    return tx_recipient, tx_amount


def get_user_choice():
    user_input = input("Your choise: ")
    return user_input


def print_blockchain_elements():
    # Result of the code.
    for block in blockchain:
        print("Outputting Block")
        print(block)
    else:
        print("-" * 20)


def verify_the_chain():
    """ Verify the current blockchain and return True if it's value, False if it's not. """
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


wait_for_input = True
# User "interface"
while wait_for_input:
    print("Please select")
    print("1: Add a new transaction value")
    print("2: Mine a new block")
    print("3: Output the blockchain blocks")
    print("h: Manipulate the chain")
    print("e: Exit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        # Add the transaction amount to the blockchain
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == "3":
        print_blockchain_elements()
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = {'previous_hash': '', 'index': 0, 'transactions': [{'sender': 'Anonymous', 'recipient': 'None', 'amount': 10000}]}
    elif user_choice == "e":
        wait_for_input = False
    else:
        print("Your input was invalid. Please try again.")
    if not verify_the_chain():
        print_blockchain_elements()
        print("Invalid hash! Code Exit")
        break   
else: 
    print("Done")
