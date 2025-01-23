# https://www.acmicpc.net/problem/2179
import sys
input = sys.stdin.readline

N = int(input())
s = [input().rstrip() for _ in range(N)]

result_value = 0
result = []
for i in range(N):
    for j in range(i+1,N):
        si = s[i]
        sj = s[j]
        min_value = min(len(si),len(sj))
        max_value = 0
        length = 0
        for k in range(min_value):
            if si[k] != sj[k]:
                max_value = max(max_value, length)
                break
            else:
                length += 1

        if length == min_value:
            max_value = max(max_value, length)

        if result_value < max_value:
            result = [si,sj]
            result_value = max_value

print(result[0])
print(result[1])
