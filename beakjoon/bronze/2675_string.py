import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m, s = map(str, input().split())

    result = ""
    for i in range(len(s)):
        for j in range(int(m)):
            result += s[i]
    print(result)