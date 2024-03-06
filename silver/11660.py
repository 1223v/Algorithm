import sys
n, m = map(int,sys.stdin.readline().split())

sumA = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
pointL = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]


print(pointL)
print(sumA)
sumL = [[0 for _ in range(n)] for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        cnt += sumA[i][j]
        sumL[i][j] = cnt

print(sumL)
# x2,y2 - x1,y1 로직
for i in range(m):
    # print(sumL[(pointL[i][3])-1][(pointL[i][2])-1])
    # print(sumL[(pointL[i][1])-1][(pointL[i][0])-1])
    if(sumL[(pointL[i][3])-1][(pointL[i][2])-1] == sumL[(pointL[i][1])-1][(pointL[i][0])-1]):
        print(sumL[(pointL[i][3]) - 1][(pointL[i][2]) - 1])
        print("메롤")
    else:
        print(sumL[(pointL[i][3]) - 1][(pointL[i][2]) - 1] - sumL[(pointL[i][1]) - 1][(pointL[i][0]) - 1])

