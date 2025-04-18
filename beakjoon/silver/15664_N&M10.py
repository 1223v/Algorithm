import sys
input = sys.stdin.readline

N,M = map(int,input().split())
s= sorted(list(map(int,input().split())))
visited = [False] * (N+1)

def dfs(v,tmp):
    if len(tmp) == M:
        print(*tmp)
        return

    prev = 0
    for i in range(v,len(s)):
        if not visited[i] and prev != s[i]:
            visited[i] = True
            tmp.append(s[i])
            prev = s[i]
            dfs(i,tmp)
            tmp.pop()
            visited[i] = False


dfs(0,[])
