import re

text = input()
word = input()

pattern = f'\\b{word}\\b'
print(len(re.findall(pattern, text, re.IGNORECASE)))