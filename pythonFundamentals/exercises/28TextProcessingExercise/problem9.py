
text = input()
i = 0
tokens = [] # list of tuples of the form (substring, number of uses)
while i < len(text):
    token = ["", 0]
    i_start = i
    while not text[i].isdigit():
        i += 1
    token[0] = text[i_start:i]
    token[0] = token[0].upper()
    while text[i].isdigit():
        token[1] = 10*token[1] + int(text[i])
        i += 1
        if i >= len(text):
            break
    tokens.append(tuple(token))

used_symbols = [] # list of used symbols
output = []
for token in tokens:
    output.extend(list(token[0]*token[1]))

output = "".join(output)

for c in output:
    if c not in used_symbols:
        used_symbols.append(c)

print(f'Unique symbols used: {len(used_symbols)}')
print(output.replace("\n", " "))
