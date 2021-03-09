concealed = input()
command = input()

while command != 'Reveal':
    tokens = command.split(':|:')
    if tokens[0] == 'InsertSpace':
        index = int(tokens[1])
        concealed = list(concealed)
        concealed.insert(index, ' ')
        print("".join(list(concealed)))

    elif tokens[0] == 'Reverse':
        substring = tokens[1]
        if substring in ''.join(list(concealed)):
            concealed = ''.join(list(concealed))
            concealed = concealed.replace(substring, '', 1)
            concealed += substring[::-1]
            print("".join(list(concealed)))
        else:
            print('error')

    elif tokens[0] == 'ChangeAll':
        substring, replacement = tokens[1], tokens[2]
        concealed = ''.join(list(concealed))
        concealed = concealed.replace(substring, replacement)
        print("".join(list(concealed)))

    command = input()

print(f'You have a new text message: {"".join(list(concealed))}')

