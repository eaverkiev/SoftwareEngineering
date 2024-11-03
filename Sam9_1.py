class Tomato:
    states = ['Отсутствует', 'Цветение', 'Зеленый', 'Красный'] #Стадии созревания помидора

    def __init__(self, index):
        self._index = index  #Индекс помидора - защищенный атрибут (динамическое свойство)
        self._state = Tomato.states[0]  #Стадия созревания - защищенный атрибут (динамическое свойство)

    #Перевод томата на следующую стадию созревания, если он еще не созрел до последней стадии
    def grow(self):
        if self._state != Tomato.states[-1]:
            self._state = Tomato.states[Tomato.states.index(self._state) + 1]

    #Метод, возвращающий True, если томат созрел
    def is_ripe(self):
        return self._state == 'Красный'


class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(i) for i in range(num)]  #Создаем список объектов класса Tomato в количестве num штук

    #Перевод всех объектов из списка томатов на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    #Метод, возвращающий True, если все томаты из списка созрели до последней стадии
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    #Метод, очищающий список томатов после сбора урожая
    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, plant):
        self.name = name  #Имя садовника - публичный атрибут (динамическое свойство)
        self._plant = plant  #Растение, за которым ухаживает садовник - защищенный атрибут (динамическое свойство)

    #Метод, заставляющий садовника работать, из-за чего растение становится более зрелым
    def work(self):
        print(f"Садовник {self.name} ухаживает за растением")
        self._plant.grow_all()

    #Метод, позволяющий собрать урожай, если все плоды созрели
    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print(f"Садовник {self.name} собрал урожай")
        else:
            print(f"Садовник {self.name} не собрал урожай, поскольку еще не все томаты созрели")

    #Статический метод, выводящий в консоль справку по садоводству
    @staticmethod
    def knowledge_base():
        print("[Справка по садоводству]")
        print("1) Посадите томаты")
        print("2) Ухаживайте за кустом с томатами")
        print("3) Проверяйте зрелось томатов")
        print("4) Собирайте урожай, когда томаты созрели")


#1) Вызов справки по садоводству
Gardener.knowledge_base()

#2) Создаем объекты классов TomatoBush и Gardener
tomato_bush1 = TomatoBush(5)
gardener1 = Gardener("Иван", tomato_bush1)

#3) Ухаживаем за кустом с помидорами
gardener1.work()

#4) Пробуем собрать урожай, когда томаты еще не дозрели. Продолжаем ухаживать за ними
gardener1.harvest()
gardener1.work()
gardener1.work()

#5) Собираем урожай
gardener1.harvest()
