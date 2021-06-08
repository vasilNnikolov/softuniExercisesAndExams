def age_assignment(*args, **kwargs):
    ages = {}
    for name in args:
        age = kwargs.pop(name[0])
        ages[name] = age

    return ages

print(age_assignment("Peter", "George", G=26, P=19))