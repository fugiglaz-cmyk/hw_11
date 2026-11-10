class InsufficientResourcesException(Exception):
    pass


def action_in_game(required_amount: int | float, current_amount: int | float) -> str:
    """function to do some action in game
    args: required_amount: the amount of resource which needed
    current_amount: the amount of resource you have now
    return: the message of done action
    """
    if current_amount < required_amount:
        raise InsufficientResourcesException
    else:
        print("action done")


try:
    required_resources = input("Enter the resources you need: ")
    required_amount = int(input("Enter the amount of resources you need: "))
    current_amount = int(input("Enter the amount of resources you have: "))
    action_in_game(required_amount, current_amount)
except InsufficientResourcesException:
    print(f"Insufficient of {required_resources}")
