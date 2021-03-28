n = int(input())

pieces = {}

for _ in range(n):
    piece, composer, key = input().split("|")
    pieces[piece] = [composer, key]
command = input()

while command != "Stop":
    tokens = command.split("|")

    if tokens[0] == "Add":
        piece, composer, key = tokens[1], tokens[2], tokens[3]
        if piece not in pieces:
            pieces[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif tokens[0] == "Remove":
        to_remove = tokens[1]
        if to_remove in pieces:
            del pieces[to_remove]
            print(f"Successfully removed {to_remove}!")
        else:
            print(f"Invalid operation! {to_remove} does not exist in the collection.")

    elif tokens[0] == "ChangeKey":
        piece, new_key = tokens[1], tokens[2]
        if piece in pieces:
            pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

pieces = dict(sorted(pieces.items(), key=lambda p: p[0]))
for p in pieces:
    print(f"{p} -> Composer: {pieces[p][0]}, Key: {pieces[p][1]}")