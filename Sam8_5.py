class Animal:
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        print("Мяу-мяу!")

class Dog(Animal):
    def sound(self):
        print("Гав-гав!")

class Cow(Animal):
    def sound(self):
        print("Муу-ууу!")

animals = [Cat(), Dog(), Cow()]
for animal in animals:
    animal.sound()
