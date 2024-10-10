import sys
input = sys.stdin.readline

N = int(input())
s = [[0,0] for i in range(N+1)]
for i in range(1,N+1):
    ti, pi = map(int, input().split())
    s[i][0] = ti
    s[i][1] = pi
max_value = 0
def dfs(n,days, total):
    global max_value

    if days > N:
        max_value = max(max_value, total)
        return

    # 상담을 받는 경우 (상담을 끝낸 후 다음 가능한 날짜로 넘어감)
    if days + s[days][0] <= N+1:
        dfs(n+1,days + s[days][0], total + s[days][1])

    # 상담 안받음
    dfs(n+1, days+1,total)

dfs(0,1,0)

print(max_value)