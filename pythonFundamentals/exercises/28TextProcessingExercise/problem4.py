text = input()

cesars_constant = 3

output = ''
for c in text:
    output += chr(cesars_constant + ord(c))

print(output)