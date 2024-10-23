# 다시 풀어볼 문제
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

s = [input().rstrip() for _ in range(N)]

result = []
for a in range(N-7):
    for b in range(M-7):
        w1 = 0
        B2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if s[i][j] != "W":
                        w1 += 1
                    if s[i][j] != "B":
                        B2 += 1
                else:
                    if s[i][j] != "B":
                        w1 += 1
                    if s[i][j] != "W":
                        B2 += 1
        result.append(min(w1,B2))
print(min(result))




