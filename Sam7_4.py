import re

def new_text(text, banned_words):
    for word in banned_words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub('*' * len(word), text)
    return text

test_text = 'Hello, world! Python IS the programming language of thE future. My EMAIL is....\nPYTHON is awesome!!!!'
with open('input.txt', 'r') as file:
    banned_words = file.read().strip().split()
result = new_text(test_text, banned_words)
print(result)
