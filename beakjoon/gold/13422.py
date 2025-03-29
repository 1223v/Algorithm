import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):

    N, M, K = map(int,input().split()) # 집 갯수, 연속된 집 갯수, 최소 돈양

    graph = list(map(int,input().split()))

    S = [0] * (2*N+1)



    for i in range(1,2*N+1):
        S[i] = S[i-1] + graph[(i-1)%N]


    if N == M:
        if sum(graph) < K:
            print(1)
            continue

        else:
            print(0)
            continue


    cnt = 0
    for i in range(M,2*N+1):
        if i == N+M:
            break
        total = S[i] - S[i-M]
        if total < K:

            cnt += 1

    print(cnt)