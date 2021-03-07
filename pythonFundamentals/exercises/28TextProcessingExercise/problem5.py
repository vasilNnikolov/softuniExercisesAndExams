text = input()
flag = False
for c in text:
    if flag:
        print(f':{c}')
        flag = False
    if c == ':':
        flag = True
        continue
