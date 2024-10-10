def func(tpl):
    unique_tpl = sorted(set(tpl))
    if len(unique_tpl) < 4:
        return ()
    result = tuple(unique_tpl[3:])
    return result
input_data = (1, 2, 2, 2, 4, 5, 3, 3)
output_data = func(input_data)
print(func((1, 2, 2, 2, 4, 5, 3, 3)))
print(func((1, 6, 6, 1, 6, 1)))
print(func((10, 44, 33, 4, 7, 5, 3, 8, 1, 0, 7, 5, 9, 1)))