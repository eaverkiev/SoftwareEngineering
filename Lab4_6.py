def main(**kwargs):
    for i, j in kwargs.items():
        print(f"{i}. Значение = {mean(j)}")

def mean(data):
    return sum(data) / float(len(data))

if __name__ == '__main__':
    main(x=[1, 2, 3, 2], y=[3, 3, 0, 3], z=[2, 4, 4, 0], k=[4, 3, 5, 1])