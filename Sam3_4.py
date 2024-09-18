line = input('Введите предложение: ')

print('Длина предложения:', len(line))

lineLower = line.lower()
print ('Предложение в нижнем регистре:', lineLower)

letters = 'aeiouy'
count = 0
for letter in lineLower:
    if letter in letters:
        count += 1
print('Количество гласных букв в предложении:', count)

print('Измененное предложение с заменой ugly на beauty:', line.replace('ugly', 'beauty'))

if (line.startswith('The') and line.endswith('end')):
    print('Предложение начинается с "The" и заканчивается на "end"')
else:
    print('Предложение не начинается с "The" и не заканчивается на "end" одновременно')