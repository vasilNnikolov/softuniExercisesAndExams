n = int(input())

stack = []

for _ in range(n):
    command = input()
    tokens = command.split(" ")
    if tokens[0] == "1":
        stack.append(tokens[1])
    elif tokens[0] == "2":
        if len(stack) > 0:
            stack.pop()
    elif tokens[0] == "3":
        if len(stack) > 0:
            print(max([int(i) for i in  stack]))
    elif tokens[0] == "4":
        if len(stack) > 0:
            print(min([int(i) for i in  stack]))

stack = [str(int(i)) for i in stack]
print(", ".join(stack[::-1]))

