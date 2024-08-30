import sys
input = sys.stdin.readline

N, M = map(int,input().split())
A = list(map(int, input().split()))
answer = 0

def dfs(n, sm, cnt):
    global answer
    if n == N:
        if sm == M and cnt > 0:
            answer += 1
        return

    dfs(n+1, sm + A[n], cnt + 1)
    dfs(n+1, sm, cnt)



dfs(0, 0 ,0)
print(answer)