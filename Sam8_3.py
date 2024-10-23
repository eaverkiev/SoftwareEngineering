class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def info(self):
        print(f"Меня зовут {self.name}. Сколько мне лет? Мне сейчас {self.age}. Кстати, мой вес - {self.weight} кг!")

    def sound(self):
        pass

class Cat(Animal):
    def __init__(self, name, age, weight, breed):
        super().__init__(name, age, weight)
        self.breed = breed

    def sound(self):
        print("Мяу-Мяу!")

cat1 = Cat("Жасмина", 2, 5, "Сиамская")
cat1.info()
cat1.sound()