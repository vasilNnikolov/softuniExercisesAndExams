def even_odd(*args):
    return list(filter(lambda x: x%2 == (1 if args[-1] == "odd" else 0), args[:-1]))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))