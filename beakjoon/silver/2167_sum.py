import sys
input = sys.stdin.readline

N,M = map(int,input().split())

s = [[0] * (M+1)] + [[0] + list(map(int,input().split())) for _ in range(N)]
prefix_sum = [[0] * (M+1) for _ in range(N+1)]

def prefix_sum_func():
    for i in range(1,N+1):
        for j in range(1,M+1):
            prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + s[i][j]

def find_prefix_sum(x1,y1,x2,y2):
    return prefix_sum[x2][y2] - prefix_sum[x2][y1-1] - prefix_sum[x1-1][y2] + prefix_sum[x1-1][y1-1]

prefix_sum_func()
K = int(input())
for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())

    print(find_prefix_sum(x1,y1,x2,y2))
