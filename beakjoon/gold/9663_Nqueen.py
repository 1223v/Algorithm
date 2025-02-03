import sys
input = sys.stdin.readline

N = int(input())

def dfs(n):
    global result
    if n == N:
        result += 1
        return

    for i in range(N):
        if visited1[i] == visited2[n-i] == visited3[n+i] == 0:
            visited1[i], visited2[n - i], visited3[n + i] = 1,1,1
            dfs(n+1)
            visited1[i], visited2[n - i], visited3[n + i] = 0, 0, 0


visited1 = [0] * N
visited2 = [0] * (2*N)
visited3 = [0] * (2*N)
result = 0
dfs(0)
print(result)