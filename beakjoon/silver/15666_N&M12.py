import sys
input= sys.stdin.readline

N,M = map(int,input().split())

s = sorted(set(list(map(int,input().split()))))

def dfs(n,tmp,v):
    if n == M:
        print(*tmp)
        return

    for i in range(v,len(s)):
        tmp.append(s[i])
        dfs(n+1,tmp,i)
        tmp.pop()

dfs(0,[],0)
