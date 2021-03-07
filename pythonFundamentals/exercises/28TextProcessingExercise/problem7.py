text = input()
bomb_left = 0
text_list = list(text)
index = 0

while index < len(text):
    if text[index] =='>':
        bomb_left += int(text[index + 1])
        index += 1
    if bomb_left > 0:
        if text_list[index] != '>':
            text_list[index] = -1
            bomb_left -= 1
        else:
            continue
    index += 1

output = ''

for c in text_list:
    if c != -1:
        output += c

print(output)