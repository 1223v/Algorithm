def dfs(n,count, csum):
    global cnt

    if csum > K:
        return
    if n == 13:
        if count == N:
            if K == csum:
                cnt += 1
        return

    dfs(n+1,count+1, csum + s[n])
    dfs(n + 1,count, csum)


T = int(input())
s = [i for i in range(13)]


cnt = 0
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    cnt = 0
    dfs(1,0,0)
    print("#%d %d" %(test_case,cnt))

