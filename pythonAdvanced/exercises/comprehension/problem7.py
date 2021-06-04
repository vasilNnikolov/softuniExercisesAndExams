lists = input().split("|")

lists = [[x for x in list(map(lambda x: x.strip(), l.split(" "))) if len(x) > 0] for l in lists]

result = [value for l in lists[::-1] for value in l]

print(" ".join(map(str, result)))