def input_expenses():
    date = input('Введите дату: ')
    summa = input('Введите сумму расходов: ')
    info = input('Введите описание расходов: ')
    with open('expenses.txt', 'a', encoding = 'utf-8') as file:
        file.write(f'{date}, {summa}, {info}\n')

def read_expenses():
    with open('expenses.txt', 'r', encoding = 'utf-8') as file:
        for line in file:
            print(line)

while True:
    command = input('1 - добавить расходы. 2 - вывести информацию о расходах: ')
    if command == '1':
        input_expenses()
    elif command == '2':(
        read_expenses())
    else:
        print('Неверная команда')