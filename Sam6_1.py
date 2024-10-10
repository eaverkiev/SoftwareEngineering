input_date = input("Введите последовательность чисел через пробел: ")
my_list = [int(i) for i in input_date.split(' ')]
my_tuple = tuple(my_list)
print("Список из чисел: ", my_list)
print("Кортеж из чисел: ", my_tuple)