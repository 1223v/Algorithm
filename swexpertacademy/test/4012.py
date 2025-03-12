# https://glory-summer.tistory.com/168

def synergy(lst):
    total = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            total += s[lst[i]][lst[j]] + s[lst[j]][lst[i]]
    return total

def dfs(n,k):
    global min_value
    if n == N//2:
        A = []
        B = []

        for i in range(N):
            if visited[i]:
                A.append(i)
            else:
                B.append(i)

        total_A = synergy(A)
        total_B = synergy(B)

        min_value = min(min_value, abs(total_A-total_B))
        return
    for i in range(k,N):
        if not visited[i]:
            visited[i] = 1
            dfs(n+1, i+1)
            visited[i] = 0


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    s = [list(map(int,input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]

    min_value = float('inf')
    dfs(0,0)


    print(f"#{test_case} {min_value}")
