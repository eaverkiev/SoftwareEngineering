import math
def func(a, b, c):
    p = (a+b+c)/2
    result = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return result