num = int(input("Введите число в диапазоне от 0 до 10 включительно: "))
if 0 <= num <= 10:
    if 0 <= num <= 3:
        print("от 0 до 3 включительно")
    elif 3 < num < 6:
        print("от 3 до 6")
    elif 6 <= num <= 10:
        print("от 6 до 10 включительно")
else:
    print('Число не подходит по требованиям')