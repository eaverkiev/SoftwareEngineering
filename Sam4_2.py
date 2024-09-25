import random
def randomcube():
    value = random.randint(1, 6)
    print(f"Значение кубика: {value}")
    if value == 5 or value == 6:
        print("Вы победили")
    elif value == 3 or value == 4:
        randomcube()
    else:
        print("Вы проиграли")
if __name__ == '__main__':
    randomcube()