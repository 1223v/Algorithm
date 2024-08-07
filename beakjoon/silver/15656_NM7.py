import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = list(map(int, input().split()))
visited = [False] * n
s = []
A.sort()

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(n):
        if not visited[i]:

            s.append(i)
            dfs()
            s.pop()


dfs()