import re

pattern = r'(www.([a-zA-Z0-9\-]+\.)+([a-zA-Z]+))'

text = input()
while text:
    for m in re.findall(pattern, text):
        print(m[0])
    text = input()


v