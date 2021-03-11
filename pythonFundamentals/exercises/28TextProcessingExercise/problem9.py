text = input()
in_number = False
number = ""
pattern = ""
output = ""

for index, c in enumerate(text):
    if c.isdigit():
        if not in_number:
            number = ""
            in_number = True
        number += c
    if not c.isdigit() or index == len(text) - 1:
        if in_number:
            output += pattern * int(number)
            in_number = False
            pattern = ""
        pattern += c.upper()


print(f"Unique symbols used: {len(set(output))}")
print(output)