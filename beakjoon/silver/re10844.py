import sys

n = int(sys.stdin.readline())

arr = [[0] * 10 for _ in range(n)]
# 초기 배열 초기화 (0 1 1 1 1 1 1 1 1)
for i in range(1,10):
    arr[0][i] = 1
for i in range(1, n):
    arr[i][0] = arr[i-1][1]
    arr[i][9] = arr[i-1][8]
    for j in range(1,9):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]
rst = 0
for i in range(10):
    rst += arr[n-1][i]

print(rst % 1000000000)