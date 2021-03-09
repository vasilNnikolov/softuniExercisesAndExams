

text = input()
i = 0
tokens = [] # list of tuples of the form (substring, number of uses)
while i < len(text):
    token = ["", 0]
    while not text[i].isdigit():
        token[0] += text[i].upper()
        i += 1
    while text[i].isdigit():
        token[1] = 10*token[1] + int(text[i])
        i += 1
        if i >= len(text):
            break
    tokens.append(tuple(token))

used_symbols = [] # list of used symbols
output = ""
for token in tokens:
    output += token[0]*token[1]

for c in output:
    if c not in used_symbols:
        used_symbols.append(c)

print(f'Unique symbols used: {len(used_symbols)}')
print(output.replace("\n", " "))
