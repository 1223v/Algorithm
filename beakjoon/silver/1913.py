import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
di = [1,0,-1,0]
dj = [0,1,0,-1]
arr = [[0]*n for _ in range(n)]

i,j,cnt,dr = 0, 0, n*n, 0
arr[i][j] = cnt
result = [i+1,j+1]
cnt -= 1
while cnt >= 1:
    ni,nj= i + di[dr], j + dj[dr]
    if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0:
        i,j = ni ,nj
        arr[i][j] = cnt
        if arr[i][j] == m:
            result = [i+1, j+1]
        cnt -= 1

    else:
        dr = (dr + 1) % 4

for i in arr:
    print(*i)

print(*result)
