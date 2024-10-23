class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def info(self):
        print(f"Меня зовут {self.name}. Сколько мне лет? Мне сейчас {self._age}. Кстати, мой вес - {self.__weight} кг!")

    def sound(self):
        pass

cat = Animal("Мурзик", 4, 7)
print(cat._age)
cat.info()