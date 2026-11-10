import random


class InsfficienctFundsError(Exception):
    pass


class InvalidAccauntError(Exception):
    pass


def transfer_founds(sender_balance, recipient_account, amount):
    recipient_account = str(recipient_account)
    if len(recipient_account) != 8:
        raise InvalidAccauntError
    if amount <= 0:
        raise ValueError
    if sender_balance <= amount:
        raise InsfficienctFundsError


try:
    balance = int(input("Enter your balance: "))
    account = int(input("Enter account number you want to transfer: "))
    transfer = int(input("Enter amount of transfer: "))
    transfer_founds(balance, account, transfer)
except InvalidAccauntError:
    print("Invalid id accaunt")
except InsfficienctFundsError:
    print("balance isn`t enough")
else:
    print("Transfer successful")
finally:
    print(f"{random.randint(1, 10000)} transfer session over")
