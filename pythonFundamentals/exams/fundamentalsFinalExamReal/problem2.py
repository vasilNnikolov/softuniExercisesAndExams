import re
n = int(input())


def check_string(string):
    special_chars = ["$", "%"]
    tag_regexes = {"$": r"^\$[A-Z][a-z]{2,}\$", "%": r"%[A-Z][a-z]{2,}%"}
    #code_regex = r"(\[(\d+)\]\|){3}$"
    code_regex = r"\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$"
    halves = string.split(": ")
    if len(halves) != 2:
        print("Valid message not found!")
        return
    tag, code = halves[0], halves[1]
    is_valid = False
    for c in special_chars:
        if re.match(tag_regexes[c], tag) and re.match(code_regex, code):
            numbers = re.findall(code_regex, code)
            output = "".join([chr(int(i)) for i in numbers[0]])
            print(f"{tag[1:-1]}: {output}")
            is_valid = True
            continue

    if not is_valid:
        print("Valid message not found!")


for i in range(n):
    string = input()
    check_string(string)
