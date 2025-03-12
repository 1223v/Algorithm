import sys
input = sys.stdin.readline

N,M = map(int,input().split())
K = int(input())

graph = [list(map(int,input().split())) for _ in range(K)]
Di,Dj = map(int,input().split())

dong_p = 0
if Di == 1:
    dong_p = Dj
elif Di == 2:
    dong_p = N + M + (N - Dj)
elif Di == 3:
    dong_p = N * 2 + M + (M - Dj)
elif Di == 4:
    dong_p = N + Dj


result = 0
for i,j in graph:

    tmp = 0
    if i == 1:
        tmp = j
    elif i == 2:
        tmp = N + M + (N-j)
    elif i == 3:
        tmp = N * 2 + M + (M-j)
    elif i == 4:
        tmp = N + j


    result += min(abs((N * 2 + M * 2)-abs(tmp - dong_p)), abs(tmp - dong_p))



print(result)

