import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
visited = [False] * (n)
result = float('-inf')
tmp = []

def dfs(depth):
    global result
    if depth == n:
        # 무조건 종료 조건 이후 순열 계산 => 값 전달은 하지 말것 dfs 백트래킹은 경우의 수를 찿는데만 사용. 책임 과중
        ans = 0
        for i in range(n-1):
            ans += abs(A[tmp[i]] - A[tmp[i+1]])
        result = max(ans,result)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            tmp.append(i)
            dfs(depth+1)
            tmp.pop()
            visited[i] = False

dfs(0)
print(result)

