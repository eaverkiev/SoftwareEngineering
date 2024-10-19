def find_numbers(file):
    count = 0
    max_number = None

    with open(file, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                if word.isdigit():
                    count += 1
                    number = int(word)
                    if max_number is None or number > max_number:
                        max_number = number

    print(f"Количество чисел: {count}")
    if max_number is not None:
        print(f"Самое большое число: {max_number}")
    else:
        print("Чисел нет в файле")

find_numbers('input.txt')

