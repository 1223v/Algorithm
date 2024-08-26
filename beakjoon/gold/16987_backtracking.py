import sys
input = sys.stdin.readline

def dfs(n, cnt):
    global ans

    if ans >= (cnt+(N-n) * 2): # 계란이 다 깨진 경우의 최대값
        return

    if n == N: # 서로 다 부딪친 경우
        ans = max(cnt, ans)
        return

    if A[n][0] <= 0:
        dfs(n+1,cnt)

    else:
        flag = False # 만약 어떠한 상황으로 인해 continue가 지속될 경우
        for i in range(N):
            if n==i or A[i][0] <=0: # 나 자신이거나 이미 깨진 계란인 경우 다음 단계로
                continue

            flag = True
            # 계란 내구도 서로 줄이기
            A[i][0] -= A[n][1]
            A[n][0] -= A[i][1]

            # 계란 1이 깨졌거나 2가 깨졌거나
            dfs(n+1, cnt + int(A[i][0] <= 0) + int(A[n][0] <= 0))

            # 다시 복원 (모든 경우를 탐색해야 하므로)
            A[i][0] += A[n][1]
            A[n][0] += A[i][1]

        if flag == False: # 다음 계란으로는 넘겨야됌
            dfs(n+1,cnt)

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]


ans = 0
# 다음 계란, 깨진 계란의 갯수
dfs(0,0)
print(ans)