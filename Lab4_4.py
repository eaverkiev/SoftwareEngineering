def main(x, *args):
    one = x
    two = sum(args)
    three = float(len(args))

    print(f"one={one}\ntwo={two}\nthree={three}")

    return x + sum(args) / float(len(args))

if __name__ == '__main__':
    result = main(10, 0, 3, 4, -1, 5, -1, 0, 1)
    print(f"\nresult={result}")