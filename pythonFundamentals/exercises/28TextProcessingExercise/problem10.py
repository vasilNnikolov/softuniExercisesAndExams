import re
tickets = input().split(', ')
winning_chars = ['@', '#', '$', '^']
winning_regex = [f'{c}']
for ticket in tickets:
    if len(ticket) != 20:
        print(f"Invalid ticket - {ticket}")
        continue
    left_half, right_half = ticket[0:10], ticket[10:20]

