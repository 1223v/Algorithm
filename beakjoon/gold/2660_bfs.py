import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
s = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = []
min_value = sys.maxsize

while True:
    v,w = map(int,input().split())
    if v == -1 and w == -1:
        break
    s[v].append(w)
    s[w].append(v)



def bfs(n,v):
    queue = deque()
    queue.append((v,n))
    visited[v] = True

    while queue:
        x,c = queue.popleft()

        for i in s[x]:
            if not visited[i]:
                visited[i] = True
                n = c+1
                queue.append((i,n))


    return n


for i in range(1,N+1):
    visited = [False] * (N + 1)
    k = bfs(0,i)

    if k < min_value:
        min_value = k
        result = []
        result.append(i)

    elif k == min_value:
        result.append(i)

print(min_value, len(result))
print(*result)
