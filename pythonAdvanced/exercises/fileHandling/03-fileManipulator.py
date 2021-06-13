import os
command = input()

while command != "End":
    tokens = command.split("-")
    if tokens[0] == "Create":
        open(tokens[1], "w").close()

    elif tokens[0] == "Add":
        filename, content = tokens[1:]
        file = open(filename, "a")
        file.write(str(content) + "\n")
        file.close()

    elif tokens[0] == "Replace":
        filename, old_str, new_str = tokens[1:]
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                for i in range(len(lines)):
                    lines[i] = lines[i].replace(old_str, new_str)

            with open(filename, "w") as file:
                for l in lines:
                    file.write(l)

        except IOError:
            print("An error occurred")

    elif tokens[0] == "Delete":
        filename = tokens[1]
        if os.path.isfile(filename):
            os.remove(filename)
        else:
            print("An error occurred")

    command = input()

