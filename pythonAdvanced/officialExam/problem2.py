n = 5
field = []

n_targets = 0

player_x, player_y = 0, 0
for col in range(n):
    line = input().strip()
    n_targets += line.count("x")
    field.append(line.split(" "))
    if field[-1].count("A") > 0:
        player_y = col
        player_x = field[-1].index("A")


n_commands = int(input())

directions = {"left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1)}
targets_hit = []

for _ in range(n_commands):
    tokens = input().split(" ")
    if tokens[0] == "move":
        step_size = int(tokens[2])
        target_x = player_x + step_size*directions[tokens[1]][0]
        target_y = player_y + step_size*directions[tokens[1]][1]

        if 0 <= target_x < n and 0 <= target_y < n and field[target_y][target_x] == ".":
            player_y = target_y
            player_x = target_x

    if tokens[0] == "shoot":
        shot_x, shot_y = player_x, player_y
        while 0 <= shot_y < n and 0 <= shot_x < n:
            if field[shot_y][shot_x] == "x":
                field[shot_y][shot_x] = "."
                targets_hit.append([shot_y, shot_x])
                break
            shot_x += directions[tokens[1]][0]
            shot_y += directions[tokens[1]][1]
        if len(targets_hit) == n_targets:
            break


if n_targets == len(targets_hit):
    print(f"Training completed! All {n_targets} targets hit.")

else:
    print(f"Training not completed! {n_targets - len(targets_hit)} targets left.")

for t in targets_hit:
    print(t)
