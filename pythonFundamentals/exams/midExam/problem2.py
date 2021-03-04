collection = input().split(' ')

command = input()
while command != 'end':
    tokens = command.split(' ')
    if len(tokens) == 5:
        if tokens[0] == 'reverse' and tokens[1] == 'from' and tokens[3] == 'count':
            start, count = int(tokens[2]), int(tokens[4])
            reversedPart = collection[start: start + count]
            reversedPart = reversedPart[::-1]
            for i in range(start, start + count):
                collection[i] = reversedPart[i - start]
        elif tokens[0] == 'sort' and tokens[1] == 'from' and tokens[3] == 'count':
            start, count = int(tokens[2]), int(tokens[4])
            toSort = collection[start: start + count]
            toSort.sort()
            for i in range(start, start + count):
                collection[i] = toSort[i - start]
    if len(tokens) == 2:
        if tokens[0] == 'remove':
            count = int(tokens[1])
            del collection[0:count]

    command = input()

print(', '.join(collection))