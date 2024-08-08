import sys
input = sys.stdin.readline

n,m = map(int, input().split())
A = list(map(int, input().split()))
visited = [False] * n
s = []
setA = sorted(set(A))

def dfs(v):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(v,len(setA)):
        if not visited[i]:

            s.append(setA[i])
            dfs(i)
            s.pop()


dfs(0)