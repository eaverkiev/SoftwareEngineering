def funct(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)
if __name__ == '__main__':
    result = funct(10, 20, 30, 20)
    print(f"Среднее арифметическое = {result}")