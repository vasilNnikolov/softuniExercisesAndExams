message = input()

command = input()
# message = list(message)
while command != "Decode":
    tokens = command.split("|")

    if tokens[0] == "Move":
        n = int(tokens[1])
        message = message[n:] + message[:n]

    elif tokens[0] == "Insert":
        index, value = int(tokens[1]), tokens[2]
        message = message[0:index] + value + message[index:]

    elif tokens[0] == "ChangeAll":
        substring, replacement = tokens[1], tokens[2]
        message = message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {message}")

