tokens = input().split(' ')

tokens = [t for t in tokens if t != '']

def isCapital(letter):
    return ord('A') <= ord(letter) <= ord('Z')

sum = 0
for token in tokens:
    n = int(token[1:-1])
    first_letter, second_letter = token[0], token[-1]
    local_sum = n
    if isCapital(first_letter):
        local_sum /= ord(first_letter) - ord('A') + 1
    else:
        local_sum *= ord(first_letter) - ord('a') + 1
    if isCapital(second_letter):
        local_sum -= ord(second_letter) - ord('A') + 1
    else:
        local_sum += ord(second_letter) - ord('a') + 1
    sum += local_sum

print(f'{sum:.2f}')