import sys
input = sys.stdin.readline

s = [list(map(str,input().rstrip())) for _ in range(5)]

for i in range(5):
    tmp = 15-len(s[i])
    s[i] += " " * tmp

for i in range(15):
    for j in range(5):
        if s[j][i] != " ":
            print(s[j][i], end="")