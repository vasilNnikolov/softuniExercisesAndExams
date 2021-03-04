n = int(input())
students = {}  # key is student name, value is list of grades
for _ in range(n):
    name, grade = input(), float(input())
    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)

students = {name: listGrades for (name, listGrades) in students.items() if sum(listGrades) / len(listGrades) >= 4.5}

students = dict(sorted(students.items(), key=lambda x: sum(x[1]) / len(x[1]), reverse=True))

for name, grades in students.items():
    print(f'{name} -> {sum(grades) / len(grades):.2f}')
