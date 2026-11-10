class IncufficientFundsException(Exception):
    pass


def transaction(amount: int | float, balance: int | float) -> int | float:
    """function for transactions
    agrs: amount: amount of money to transfer
    balance: current balance of money
    return: message of transaction done
    """
    if balance < amount:
        raise IncufficientFundsException
    else:
        return "transaction done"


try:
    amount = int(input("Enter the amount:"))
    balance = int(input("Enter the balance:"))
    print(transaction(amount, balance))
except IncufficientFundsException:
    print("transaction failed, balance isn`t enough")
