def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for el in numbers:
        try:
            result += el
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы: {el}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        av = personal_sum(numbers)
        try:
            average_ = av[0] / (len(numbers) - av[1])
        except ZeroDivisionError:
            average_ = 0
        return average_
    except TypeError:
        print(f'В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать