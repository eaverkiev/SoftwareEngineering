def count_statistics(file):

    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    lines = text.count('\n') + 1
    words = len(text.split())
    letters = sum(1 for char in text if char.isalpha())

    print('Input file contains:')
    print(f'{letters} letters')
    print(f'{words} words')
    print(f'{lines} lines')

count_statistics('input.txt')

