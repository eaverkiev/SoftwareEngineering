list1 = [1, 1, 3, 3, 1]
list2 = [5, 5, 5, 5, 5, 5, 5]
list3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
def func(lst):
    resultSet = set()
    for number in lst:
        count = lst.count(number)
        if count > 1:
            resultSet.add(str(number) * count)
            for i in range(2, count):
                resultSet.add(str(number) * i)
        resultSet.add(number)
    return resultSet
print(func(list1))
print(func(list2))
print(func(list3))