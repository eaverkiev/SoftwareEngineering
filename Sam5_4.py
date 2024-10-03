marks1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
marks2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
marks3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
def newMarks(marks):
    i = 0
    while i < len(marks):
        if marks[i] == 2:
           marks.pop(i)
           i = i - 1
        elif marks[i] == 3:
            marks[i] = 4
        i = i + 1
    return marks
print(newMarks(marks1))
print(newMarks(marks2))
print(newMarks(marks3))
