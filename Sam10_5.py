# Определяем собственное исключение
class AccessDeniedError(Exception):
    # Исключение, вызываемое при недостаточном уровне доступа
    def __init__(self, message):
        self.message = message

# Функция для просмотра оценок
def view_grades(role):
    # Проверяем роль и бросаем исключение, если она не соответствует преподавателю или студенту
    if role.lower() != 'преподаватель' and role.lower() != 'студент':
        raise AccessDeniedError("Доступ запрещен: у вас недостаточный уровень доступа!")
    print("*Просмотр оценок*")

# Функция для выставления оценок
def set_grades(role):
    # Проверяем роль и бросаем исключение, если она не соответствует преподавателю
    if role.lower() != 'преподаватель':
        raise AccessDeniedError("Доступ запрещен: у вас недостаточный уровень доступа!")
    print("*Выставление оценок*")

# Главная функция программы
def func(name, role):
    try:
        # Попытка просмотра оценок
        print(f"{name} пытается просмотреть оценки")
        view_grades(role)
    except AccessDeniedError as e:
        print(e)

    try:
        # Попытка выставления оценок
        print(f"{name} пытается выставить оценки")
        set_grades(role)
    except AccessDeniedError as e:
        print(e)

# Тестируем программу
if __name__ == "__main__":
    func("Виктор", "Студент")
    func("Николай", "преподаватель")
    func("Иван", "пользователь")