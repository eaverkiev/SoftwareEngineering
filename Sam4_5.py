from Square import func
print("Введите длины сторон треугольника: ")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
result = func(a, b, c)
print(f"Площадь треугольника = {result}")