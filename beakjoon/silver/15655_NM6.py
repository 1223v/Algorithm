import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = list(map(int,input().split()))
visited = [False] * (n)
s = []
A.sort()
def dfs(v):

    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(v,n):
        if not visited[i]:
            visited[i] = True
            s.append(A[i])
            dfs(i+1)
            s.pop()
            visited[i] = False


dfs(0)
