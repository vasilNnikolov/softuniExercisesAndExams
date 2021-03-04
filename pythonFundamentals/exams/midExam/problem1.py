experience = float(input())

numberOfBattles = int(input())

for i in range(1, numberOfBattles + 1):
    gained = float(input())
    bonus = 0
    if i%3 == 0:
        bonus += 15
    if i%5 == 0:
        bonus -= 10
    gained = gained*(1 + bonus/100)
    experience -= gained
    if experience <= 0:
        print(f'Player successfully collected his needed experience for {i} battles.')
        break

if experience > 0:
    print(f'Player was not able to collect the needed experience, {experience:.2f} more needed.')