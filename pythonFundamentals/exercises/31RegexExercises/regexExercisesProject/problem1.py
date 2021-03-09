import re

regex = r'(\d+)'

line = input()
output = []
while line:
    matches = re.findall(regex, line)
    output.extend(matches)
    line = input()

print(' '.join(output))