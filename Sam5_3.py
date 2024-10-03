import math
one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]
def square(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
maxSquare = square(max(one), max(two), max(three))
minSquare = square(min(one), min(two), min(three))
print(f"Площадь треугольника с максимальными сторонами: {maxSquare}")
print(f"Площадь треугольника с минимальными сторонами: {minSquare}")