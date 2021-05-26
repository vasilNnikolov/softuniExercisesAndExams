bullet_price = int(input())

barrel_size = int(input())

bullet_radius = input().split()
bullet_radius = list(map(int, bullet_radius))

lock_radius = input().split()
lock_radius = list(map(int, lock_radius))

intel_value = int(input())

bullets_in_gun = barrel_size
bullets_used = 0
while len(bullet_radius) > 0 and len(lock_radius) > 0:
    if bullet_radius[-1] <= lock_radius[0]:
        print("Bang!")
        lock_radius.pop(0)
    else:
        print("Ping!")

    bullet_radius.pop(-1)
    bullets_used += 1
    bullets_in_gun -= 1

    if bullets_in_gun == 0 and len(bullet_radius) > 0:
        print("Reloading!")
        bullets_in_gun = barrel_size


if len(lock_radius) == 0:
    print(f"{len(bullet_radius)} bullets left. Earned ${intel_value - bullets_used*bullet_price}")
else:
    print(f"Couldn't get through. Locks left: {len(lock_radius)}")
