def func(tpl, number):
    if number in tpl:
        pos = tpl.index(number)
        return tpl[:pos] + tpl[pos + 1:len(tpl)]
    return tpl
print(func((1, 5, 7, 3, 4), 5))
print(func((2, 4, 3, 4, 2, 3, 5), 4))
print(func((1, 2, 3, 7, 5), 9))