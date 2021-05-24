closing = {"(": ")", "[": "]", "{": "}"}

string = input()
def is_balanced(string):
    stack = []
    for index, c in enumerate(string):
        if c in closing.keys():
            stack.append(c)
        else:
            if len(stack) == 0:
                return "NO"
            if closing.get(stack[-1]) == c:
                stack.pop()
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"

print(is_balanced(string))

