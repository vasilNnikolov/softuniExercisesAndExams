# has some bug, judge gives 85/100
males = [int(i) for i in input().split(" ")]
females = [int(i) for i in input().split(" ")]

males = [m for m in males if m > 0 and m%25 != 0]
females = [f for f in females if f > 0 and f%25 != 0]

males = males[::-1]
match_count = 0

while len(males) > 0 and len(females) > 0:
    first_female, last_male = females[0], males[0]
    if first_female == last_male:
        females.pop(0)
        males.pop(0)
        match_count += 1

    else:
        females.pop(0)
        males[0] -= 2
        if males[0] <= 0:
            males.pop(0)

    for male_index, male in enumerate(males):
        if male%25 == 0:
            males.pop(male_index)
            if 0 <= male_index < len(males):
                males.pop(male_index)

    for female_index, female in enumerate(females):
        if female % 25 == 0:
            females.pop(female_index)
            if 0 <= female_index < len(females):
                females.pop(female_index)

print(f"Matches: {match_count}")

if len(males) == 0:
    print("Males left: none")
else:
    print(f"Males left: {', '.join([str(m) for m in males])}")

if len(females) == 0:
    print("Females left: none")
else:
    print(f"Females left: {', '.join([str(f) for f in females])}")

