import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = list(map(int,input().split()))
visited = [False] * n
s = []

setA = sorted(set(A))

def dfs():
    if len(s) == m:
        print(' '.join(map(str,s)))
        return

    for i in range(len(setA)):
        if not visited[i]:
            s.append(setA[i])
            dfs()
            s.pop()

dfs()