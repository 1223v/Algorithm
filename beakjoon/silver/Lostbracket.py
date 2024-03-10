import sys

n = sys.stdin.readline().rstrip().split('-')

sum = 0
for i in n[0].split('+'):
    sum += int(i)

for i in n[1:]:
    for j in i.split('+'):
        sum -= int(j)

print(sum)