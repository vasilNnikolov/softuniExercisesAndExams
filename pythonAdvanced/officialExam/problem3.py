def math_operations(*args, **kwargs):
    args = list(args)
    operations = ["a", "s", "d", "m"]
    current_index = 0
    operation_index = 0
    while current_index < len(args):
        operation_index = operation_index%4
        if operation_index == 0: # add
            kwargs["a"] += args[current_index]

        elif operation_index == 1: # subtract
            kwargs["s"] -= args[current_index]

        elif operation_index == 2: # divide
            if args[current_index] == 0:
                args.pop(current_index)
                current_index -= 1
            else:
                kwargs["d"] /= args[current_index]

        elif operation_index == 3: # multiply
            kwargs["m"] *= args[current_index]

        current_index += 1
        operation_index += 1

    return kwargs




print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))