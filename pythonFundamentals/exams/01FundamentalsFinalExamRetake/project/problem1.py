message = input()

command = input()
message = list(message)
while command != "Decode":
    tokens = command.split("|")

    if tokens[0] == "Move":
        n = int(tokens[1])
        message = message[n:] + message[:n]

    elif tokens[0] == "Insert":
        index, value = int(tokens[1]), tokens[2]
        message.insert(index, value)

    elif tokens[0] == "ChangeAll":
        substring, replacement = tokens[1], tokens[2]
        message = "".join(message)
        message = message.replace(substring, replacement)
        message = list(message)

    command = input()

print(f"The decrypted message is: {''.join(message)}")

