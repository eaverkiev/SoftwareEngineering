def add_two():
    number = input("Введите число: ")
    try:
        result = 2 + float(number)
        print(f"Результат: {result}")
    except ValueError:
        print('Неподходящий тип данных. Ожидалось число.')

add_two()
add_two()
add_two()
add_two()