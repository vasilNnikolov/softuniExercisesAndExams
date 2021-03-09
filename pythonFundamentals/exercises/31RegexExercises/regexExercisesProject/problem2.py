import re

pattern = r'\b_([a-zA-Z0-9]+)\b'

text = input()

print(','.join(re.findall(pattern, text)))