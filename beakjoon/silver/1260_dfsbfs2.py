import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int,input().split())
lst = [[] for _ in range(n+1)]

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)
s_dfs= []
s_bfs = []

for i in range(m):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)

for i in lst:
    i.sort()
def dfs(x):

    visited_dfs[x] = True
    s_dfs.append(x)

    for i in lst[x]:
        if not visited_dfs[i]:
            dfs(i)


def bfs(x):

    queue = deque()
    queue.append(x)
    visited_bfs[x] = True
    s_bfs.append(x)
    while queue:
        x = queue.popleft()

        for i in lst[x]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                s_bfs.append(i)
                queue.append(i)





dfs(v)
bfs(v)
print(*s_dfs)
print(*s_bfs)