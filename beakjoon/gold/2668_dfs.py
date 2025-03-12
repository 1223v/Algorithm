# 인데스와 배열값이 일치하는 집합의 갯수 최대 구하기

import sys
input = sys.stdin.readline

N = int(input())
result = []
s = [0] + [int(input()) for _ in range(N)]


def dfs(v,i):

    visited[v] = True
    w = s[v]
    if not visited[w]:
        dfs(w,i)

    elif visited[w] and w == i:
        result.append(w)


for i in range(1,N+1):
    visited = [False] * (N+1)
    dfs(i,i)

result.sort()
print(len(result))
print('\n'.join(map(str,result)))
