command = input()
courses = {} # key is course name, value is array of students enrolled
while command != 'end':
    courseName, studentName = command.split(' : ')
    if courseName in courses:
        courses[courseName].append(studentName)
    else:
        courses[courseName] = [studentName]
    command = input()

courses = dict(sorted(courses.items(), key=lambda x: len(x[1]), reverse=True))
for courseName, students in courses.items():
    print(f'{courseName}: {len(students)}')
    students.sort()
    for s in students:
        print(f'-- {s}')