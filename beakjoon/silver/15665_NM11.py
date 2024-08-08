import sys
input = sys.stdin.readline

n,m = map(int, input().split())
A = list(map(int, input().split()))
visited = [False] * n
s = []
sortA = sorted(set(A))


def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(len(sortA)):
        if not visited[i]:

            s.append(sortA[i])
            dfs()
            s.pop()



dfs()