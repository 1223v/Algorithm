import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = list(map(int, input().split()))
visited = [False] * (len(A))
k = []
A.sort()

def dfs():

    if len(k) == m:
        print(' '.join(map(str,k)))
        return

    for i in range(len(A)):
        if not visited[i]:
            k.append(A[i])
            visited[i] = True
            dfs()
            k.pop()
            visited[i] = False

dfs()