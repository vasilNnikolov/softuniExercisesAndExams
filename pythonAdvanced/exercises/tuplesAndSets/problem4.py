text = input()

chars = set(list(text))

occurances = {c: text.count(c) for c in chars}

occurances = dict(sorted(occurances.items(), key=lambda c: c[0]))

for c in occurances:
    print(f"{c}: {occurances[c]} time/s")