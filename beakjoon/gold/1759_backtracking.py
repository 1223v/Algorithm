# 난해
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n,m = map(int,input().split())
A = list(input().split())
visited = [False] *(m)
sort_A= sorted(A)
result = []
aeiou = ["a","e","i","o","u"]

def dfs(v):
    if len(result) == n:
        if any(char in result for char in aeiou) and (len(result) - sum(1 for char in aeiou if char in result)) >= 2:
            print(''.join(map(str, result)))
        return
    for i in range(v,m):
        if not visited[i]:
            visited[i] = True
            result.append(sort_A[i])
            dfs(i)
            visited[i] = False
            result.pop()


dfs(0)