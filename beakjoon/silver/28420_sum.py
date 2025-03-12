import sys
input = sys.stdin.readline

N,M = map(int,input().split())
a,b,c = map(int,input().split())
s = [[0] * (M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
s_sum = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        s_sum[i][j] = s_sum[i][j-1] + s_sum[i-1][j] - s_sum[i-1][j-1] + s[i][j]

def prefix_sum(x1,y1,x2,y2):
    return s_sum[x2][y2] - s_sum[x1-1][y2] - s_sum[x2][y1-1] + s_sum[x1-1][y1-1]

result = sys.maxsize
for y in range(1,N-a+2):
    for x in range(1,M-b-c+2):
        # v2 = | x,y -> x+b+c-1, y+a-1|
        result = min(result, prefix_sum(y,x,y+a-1,x+b+c-1))


for i in range(1,N-a-b+2):
    for j in range(1, M - c - a + 2):
        result = min(result, prefix_sum(i,j,i+a-1,j+c-1) + prefix_sum(i+a,j+c, i+a+b-1, j+a+c-1))

for i in range(1, N-a-c+2):
    for j in range(1,M-b-a+2):
        result = min(result, prefix_sum(i,j, i+a-1, j+b-1)+ prefix_sum(i+a, j+b, i+a+c-1, j+a+b-1))





print(result)