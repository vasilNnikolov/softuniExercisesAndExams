submissions = {} # key is username, value is array of tuples language-points
command = input()

banned = []
while command != 'exam finished':
    tokens = command.split('-')
    if len(tokens) == 3:
       username, language, points = tokens[0], tokens[1], int(tokens[2])
       if username not in submissions:
           submissions[username] = [(language, points)]
       else:
           submissions[username].append((language, points))
    elif len(tokens) == 2:
        banned.append(tokens[0])
    command = input()
submissions = dict(sorted(submissions.items(), key=lambda x: x[0]))
submissions = dict(sorted(submissions.items(), key=lambda x: max([p[1] for p in x[1]]), reverse=True))
print('Results:')
for username, results in submissions.items():
    if username not in banned:
        print(f'{username} | {max([p[1] for p in results])}')

print('Submissions:')
languages = {} # key is language name, value is number of submissions

for results in submissions.values():
    for r in results:
        language = r[0]
        if language not in languages:
            languages[language] = 1
        else:
            languages[language] += 1

languages = dict(sorted(languages.items(), key=lambda x: x[0]))
languages = dict(sorted(languages.items(), key=lambda x: x[1], reverse=True))

for language, nSubmissions in languages.items():
    print(f'{language} - {nSubmissions}')
