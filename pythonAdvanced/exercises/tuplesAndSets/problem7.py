n = int(input())

odds, evens = set(), set()

for line_index in range(1, n + 1):
    name = input()
    name_sum = sum([ord(c) for c in name]) // line_index
    if name_sum % 2 == 0:
        evens.add(name_sum)
    else:
        odds.add(name_sum)

odd_sum = sum(odds)
even_sum = sum(evens)

if odd_sum == even_sum:
    print(", ".join(list(map(str, odds.union(evens)))))

elif odd_sum > even_sum:
    print(", ".join(list(map(str, odds.difference(evens)))))

elif odd_sum < even_sum:
    print(", ".join(list(map(str, odds.symmetric_difference(evens)))))



