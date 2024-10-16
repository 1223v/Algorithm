import sys
input = sys.stdin.readline

n, m = map(int,input().split())
s = [input().rstrip() for _ in range(n)]
k = ["" for _ in range(m)]

count = 0
for i in range(n):
    tmp = s[i].split('|')
    filtered_tmp = [j for j in tmp if j != '']
    count += len(filtered_tmp)


for i in range(m):
    for j in range(n):
        k[i] += s[j][i]

for i in range(m):
    tmp = k[i].split('-')
    filtered_tmp = [j for j in tmp if j != '']
    count += len(filtered_tmp)

print(count)