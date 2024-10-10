def func(tpl, number):
    if number in tpl:
        pos1 = tpl.index(number)
        new_tpl = tpl[pos1:]
        if number in new_tpl[1:]:
            pos2 = new_tpl[1:].index(number) + 1
            return new_tpl[:pos2 + 1]
        return new_tpl
    return ()

print(func((1, 2, 3), 8))
print(func((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(func((1, 2, 8, 5, 1, 2, 9), 8))