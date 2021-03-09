# tokens = input().split(' ')
#
# tokens = [t for t in tokens if len(t) > 0]
import re

pattern = r'([a-zA-Z][-0-9\s]{1,}[a-zA-Z])'
tokens = re.findall(pattern, input())
sum = 0
for token in tokens:
    number = token[1:-1]
    number = number.replace(" ", "")
    n = float(number)
    first_letter, second_letter = token[0], token[-1]
    local_sum = n
    if ord("A") <= ord(first_letter) <= ord("Z"):
        local_sum /= ord(first_letter) - ord('A') + 1

    if ord("a") <= ord(first_letter) <= ord("z"):
        local_sum *= ord(first_letter) - ord('a') + 1

    if ord("A") <= ord(second_letter) <= ord("Z"):
        local_sum -= ord(second_letter) - ord('A') + 1

    if ord("a") <= ord(second_letter) <= ord("z"):
        local_sum += ord(second_letter) - ord('a') + 1

    sum += local_sum

print(f'{sum:.2f}')