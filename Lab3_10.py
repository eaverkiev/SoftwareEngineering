arr = [2, 4, 6, 8, 9]
flag = False
for value in arr:
    if value % 2 == 1:
        flag = True
if flag:
    print('В массиве есть нечетное число')
else:
    print('В массиве нет нечетных чисел')