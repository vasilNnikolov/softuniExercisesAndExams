import re

winning_chars = ['@', '#', '$', '^']
jackpot_regex = {c: f"(\{c}){{10}}" for c in winning_chars}
winning_regex = {c: f"(\{c}{{6,9}})" for c in winning_chars}

tickets = input().split(', ')
tickets = [t.strip() for t in tickets]

for ticket in tickets:
    if len(ticket) != 20:
        print('invalid ticket')
        continue
    else:
        is_winning = False
        left_half, right_half = ticket[0:10], ticket[10:20]

        for c in winning_chars:
            if bool(re.search(jackpot_regex[c], left_half)) and bool(re.search(jackpot_regex[c], right_half)):
                # jackpot
                print(f"ticket \"{ticket}\" - 10{c} Jackpot!")
                is_winning = True
                break

            simple_win = bool(re.search(winning_regex[c], left_half)) and bool(re.search(winning_regex[c], right_half))
            left_jackpot = bool(re.search(jackpot_regex[c], left_half)) and bool(re.search(winning_regex[c], right_half))
            right_jackpot = bool(re.search(winning_regex[c], left_half)) and bool(re.search(jackpot_regex[c], right_half))

            if bool(simple_win) or bool(left_jackpot) or bool(right_jackpot):
                # normal win
                # print(f"ticket \"{ticket}\" - {max(len(re.findall(winning_regex[c], left_half)[0]), len(re.findall(winning_regex[c], right_half)[0]))}{c}")
                if len(re.findall(winning_regex[c], left_half)[0]) == len(re.findall(winning_regex[c], right_half)[0]):
                    print(f"ticket \"{ticket}\" - {len(re.findall(winning_regex[c], left_half)[0])}{c}")
                    is_winning = True
                    break

        if not is_winning:
            print(f"ticket \"{ticket}\" - no match")

