text = input()
current_letter = text[0]
output = current_letter
for c in text:
    if c != current_letter:
        output += c
        current_letter = c

print(output)