def analyze_text(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
            words = text.split()
            word_count = len(words)
            frequency = {}

            for word in words:
                word = word.lower()
                if word in frequency:
                    frequency[word] += 1
                else:
                    frequency[word] = 1

            most_common_word = ""
            most_common_count = 0
            for word, count in frequency.items():
                if count > most_common_count:
                    most_common_count = count
                    most_common_word = word

            print(f'Количество слов в файле: {word_count}')
            print(f'Самое часто встречающееся слово: {most_common_word}. Оно встречается {most_common_count} раз')

    except Exception as e:
        print("Произошла ошибка:", str(e))

analyze_text('input.txt')