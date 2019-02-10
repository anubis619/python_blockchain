# Initializing our blockchain list
blockchain = []


# Function definitions
def get_blockchain_value():
    """ Returns the last value of the current blockain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """Append a new value as well as the last blockchain value to the blockchain


    Arguments:
        :transaction_amount: => The amout that should be added
        :last_transaction: => The last blockchain value. Default ([1])
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    return float(input("Please enter the amount of the transaction: "))


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
    #block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        if blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        # block_index += 1
    return is_valid


wait_for_input = True
# User "interface"
while wait_for_input:
    print("Please select")
    print("1: Add a new transaction value")
    print("2: Output the blockchain blocks")
    print("h: Manipulate the chain")
    print("e: Exit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_user_amount = get_transaction_value()
        add_transaction(tx_user_amount, get_blockchain_value())
    elif user_choice == "2":
        print_blockchain_elements()
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == "e":
        wait_for_input = False
    else:
        print("Your input was invalid. Please try again.")
    if not verify_the_chain():
        print_blockchain_elements()
        print("Invalid hash! Code Exit")
        break        


print("Done")
