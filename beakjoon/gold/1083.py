import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
s = int(input())

for i in range(N):
    # 탐색
    max_num = max(A[i:min(N,i+s+1)])
    idx = A.index(max_num)

    # 정렬
    for j in range(idx,i,-1):
        A[j],A[j-1] = A[j-1],A[j]

    s -= idx - i
    if s <= 0:
        break

print(*A)