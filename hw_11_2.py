def read_numbers(filename: str) -> list:
    """function to read the whole numbers of the file
    args: filename: the file to read
    return: a list of numbers
    """
    numbers = []
    with open(filename, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            for token in line.replace(",", " ").split():
                try:
                    numbers.append(float(token))
                except ValueError:
                    raise ValueError(f"нечислове значення '{token}' у рядку {line_number}")
    return numbers


def main() -> str:
    """Function to load the whole algorithm
    return: len of read numbers and the average of it
    """
    filename = input("Введіть ім'я файлу: ").strip()

    try:
        numbers = read_numbers(filename)
    except FileNotFoundError:
        print(f"Помилка: файл '{filename}' не знайдено.")
        return
    except ValueError as error:
        print(f"Помилка: у файлі містяться нечислові дані ({error}).")
        return

    if not numbers:
        print("Файл не містить жодного числа, середнє обчислити неможливо.")
        return

    average = sum(numbers) / len(numbers)
    print(f"Прочитано чисел: {len(numbers)}")
    print(f"Середнє арифметичне: {average}")
