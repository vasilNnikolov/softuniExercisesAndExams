email = input()

command = input()

while command != "Complete":
    tokens = command.split(" ")
    if tokens[0] == "Make":
        if tokens[1] == "Lower":
            email = email.lower()
            print(email)
        elif tokens[1] == "Upper":
            email = email.upper()
            print(email)

    elif tokens[0] == "GetDomain":
        count = int(tokens[1])
        print(email[-count:])

    elif tokens[0] == "GetUsername":
        if "@" in email:
            print(email[:email.find("@")])
        else:
            print(f"The email {email} doesn't contain the @ symbol.")

    elif tokens[0] == "Replace":
        email = email.replace(tokens[1], "-")
        print(email)

    elif tokens[0] == "Encrypt":
        for c in email:
            print(ord(c), end=" ")

    command = input()


