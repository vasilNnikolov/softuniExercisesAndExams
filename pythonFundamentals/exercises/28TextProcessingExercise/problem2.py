a, b = input().split(' ')

sum = 0
for i in range(min(len(a), len(b))):
    sum += ord(a[i])*ord(b[i])

longer = a
if len(b) > len(a):
    longer = b

for j in range(min(len(a), len(b)), len(longer)):
    sum += ord(longer[j])

print(sum)