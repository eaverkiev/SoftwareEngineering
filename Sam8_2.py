class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def info(self):
        print(f"Меня зовут {self.name}. Сколько мне лет? Мне сейчас {self.age}. Кстати, мой вес - {self.weight} кг!")

    def sound(self):
        pass

cat = Animal("Барсик", 2, 5)
cat.info()