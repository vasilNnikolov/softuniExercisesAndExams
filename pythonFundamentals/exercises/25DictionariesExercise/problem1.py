string = input()

letters = {}

for c in string:
    if c != ' ':
        if c in letters.keys():
            letters[c] += 1
        else:
            letters[c] = 1

for key, value in letters.items():
    print(f'{key} -> {value}')