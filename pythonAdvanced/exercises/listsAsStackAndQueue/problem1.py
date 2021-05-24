
numbers = input()
if len(numbers) > 0:
    numbers = numbers.split(" ")
    if len(numbers) > 0:
        #numbers = [int(n) for n in numbers]

        # stack = []
        #
        # for n in numbers:
        #     stack.append(n)
        # while len(stack) > 0:
        #     print(f"{stack.pop(-1)} ", end="")

        numbers = numbers[::-1]
        for n in numbers:
            print(f"{n} ", end="")

