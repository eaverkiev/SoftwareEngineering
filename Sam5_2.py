results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9,
           27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]
results.sort()
best = results[:3]
worst = results[-3:]
results10 = [element for element in results if element >= 10]
print(f"Три лучших результата: {best}")
print(f"Три худших результата: {worst}")
print(f"Все результаты начиная с 10: {results10}")