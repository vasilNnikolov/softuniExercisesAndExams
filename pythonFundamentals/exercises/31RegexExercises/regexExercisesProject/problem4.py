import re

host_pattern = r'(\w+([\.\-_]*\w+[\.\-_]*)*\w+)'
domain_pattern = r'(\w+([\.\-]*\w+[\.\-]*)*\w+\.\w+([\.\-]*\w+[\.\-]*)*\w+)'

email_pattern = r'\b' + '(' + host_pattern + '@' + domain_pattern + ')' + r'[\.\b]{1}'
# email_pattern = '(' + host_pattern + '@' + domain_pattern + ')'

text = input()

matches = re.findall(email_pattern, text)
for m in matches:
    print(m[0])