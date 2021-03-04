
names = input().split(', ')

for name in names:
    if 3 <= len(name) <= 16 and [l.isalpha() or l.isdigit() or l == '-' or l == '_' for l in name] == [True]*len(name):
        print(name)
