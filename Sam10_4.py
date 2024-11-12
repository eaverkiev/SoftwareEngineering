# Определяем класс декоратора
class ArrayStats:
    # Метод, который вызовется при создании класса (конструктор)
    def __init__(self, func):
        self.func = func

    # Метод, вызываемый при обращении к декорированной функции
    def __call__(self, arr):
        # Вызываем оригинальную функцию и получаем результат
        result = self.func(arr)

        # Вычисляем минимальное, максимальное и среднее значения
        if result:  # Проверяем, что результат не пустой
            min_val = min(result)
            max_val = max(result)
            avg_val = sum(result) / len(result)
            print(f'Минимальное число: {min_val}')
            print(f'Максимальное число: {max_val}')
            print(f'Среднее число: {avg_val:.2f}\n')
        else:
            print('Массив пуст.\n')

        return result

# Функция для сортировки списка
@ArrayStats
def sort_func(arr):
    n = len(arr)

    # Сортируем список
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Функция для удаления отрицательных чисел из списка
@ArrayStats
def delete_negative(arr):
    return [x for x in arr if x >= 0]

# Тестируем функции
if __name__ == "__main__":
    # Исходный список
    array = [5, -10, 25, 0, 34, 11, -40, -3]

    print("Сортировка списка:")
    sorted_array = sort_func(array)
    print(f'Отсортированный список: {sorted_array}')

    print("\nУдаление отрицательных чисел:")
    non_negative_array = delete_negative(array)
    print(f'Список неотрицательных чисел: {non_negative_array}')