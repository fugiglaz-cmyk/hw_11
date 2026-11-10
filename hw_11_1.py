class UnknownOperationError(Exception):
    pass


def calculator(num1: int | float, action: str, num2: int | float) -> int | float:
    """calculator function
    args: num1: first number
    num2: second number
    action: action you want to do
    return: calculated number
    """
    if action == '+':
        return num1 + num2
    elif action == '-':
        return num1 - num2
    elif action == '*':
        return num1 * num2
    elif action == '/':
        return num1 / num2
    elif action == '**':
        return num1 ** num2
    elif action == "//":
        return num1 // num2
    elif action == "%":
        return num1 % num2
    else:
        raise UnknownOperationError


try:
    num1 = int(input("Enter first number: "))
    action = input("Enter action: ")
    num2 = int(input("Enter second number: "))
    print(calculator(num1, action, num2))
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Invalid input")
except UnknownOperationError:
    print("Invalid operation")
