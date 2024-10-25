import sys
input = sys.stdin.readline

N, K = map(int,input().split())
S = [i for i in range(1,N+1)]

result = []
idx = 0
while S:
    idx += K -1
    if idx >= len(S):
        idx %= len(S)

    result.append(S.pop(idx))

print("<"+ ", ".join(map(str, result))+ ">")