tickets = [t.strip() for t in input().split(", ")]

def is_winning(ticket):
    if len(ticket) != 20:
        return ("invalid ticket", 0)

    else:
        left_half, right_half = ticket[0:10], ticket[10:20]

        winning_chars = "$@#^"
        for winning_char in winning_chars:
            if winning_char*6 in left_half and winning_char*6 in right_half:
                best_count = 6
                for n in range(6, 11):
                    if winning_char*n in left_half and winning_char*n in right_half:
                        best_count = n
                    else:
                        break
                return (winning_char, best_count)

        return ("no match", 0)


for ticket in tickets:
    tokens = is_winning(ticket)
    if tokens[0] == "invalid ticket":
        print("invalid ticket")

    elif tokens[0] == "no match":
        print(f"ticket \"{ticket}\" - no match")

    else:
        if 6 <= tokens[1] <= 9:
            print(f"ticket \"{ticket}\" - {tokens[1]}{tokens[0]}")

        if tokens[1] == 10:
            print(f"ticket \"{ticket}\" - 10{tokens[0]} Jackpot!")
