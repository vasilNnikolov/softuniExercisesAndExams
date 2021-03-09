import re

chars = ['@', '#']

patterns = [f'{c}([a-zA-Z]{{3,}}){c}{c}([a-zA-Z]{{3,}}){c}' for c in chars]

text = input()
matches = {} # key is position of match, value is groups
for pattern in patterns:
    for match in re.finditer(pattern, text):
        matches[match.start()] = match.groups()

matches = dict(sorted(matches.items(), key=lambda x: x[0]))
mirrors = []
for m in matches.values():
    if m[0] == m[1][::-1]:
        mirrors.append(m[0])

if len(matches) == 0:
    print('No word pairs found!')
    print('No mirror words!')
else:
    print(f'{len(matches)} word pairs found!')
    if len(mirrors) == 0:
        print('No mirror words!')
    else:
        print('The mirror words are:')
        print(', '.join([f'{m} <=> {m[::-1]}' for m in mirrors]))