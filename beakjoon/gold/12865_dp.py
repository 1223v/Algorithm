import sys
input = sys.stdin.readline

N, K = map(int,input().split())
tbl = [0] * (K+1)
for i in range(N):
    W, V = map(int, input().split())
    if W > K:
        continue
    for j in range(K, 0, -1):
        if j + W <= K and tbl[j] != 0:
            tbl[j+W] = max(tbl[j+W], tbl[j]+V)
    tbl[W] = max(tbl[W], V)
print(max(tbl))