import sys
input = sys.stdin.readline

N,M,ci,cj,K = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
lst = list(map(int,input().split()))

di = [0,0,0,-1,1] # 1부터 시작이므로 5개
dj = [0,1,-1,0,0] # 동 -> 서 -> 북 -> 남

n1,n2,n3,n4,n5,n6 = 0,0,0,0,0,0

alst = []

for i in lst:

    # [1] 이동 후, 범위 내이면, 처리
    ni,nj = ci + di[i], cj + dj[i]
    if 0 <= ni < N and 0 <= nj < M:
        # [2] 주사위 굴리기

        if i == 1:  # 동
            n1,n3,n4,n6 = n4,n1,n6,n3

        elif i == 2: # 서
            n1,n3,n4,n6 = n3,n6,n1,n4

        elif i == 3: # 북
            n1,n2,n5,n6 = n5,n1,n6,n2

        else:   #남
            n1,n2,n5,n6 = n2,n6,n1,n5

        # [3] 바닥 체크
        if arr[ni][nj] == 0:
            arr[ni][nj] = n6

        else:
            n6 = arr[ni][nj]
            arr[ni][nj] = 0

        alst.append(n1)
        ci,cj = ni,nj

print(*alst,sep='\n')
