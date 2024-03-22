n, m = map(int,input().split())

AL = [list(map(int,input())) for _ in range(n)]
BL = [list(map(int,input())) for _ in range(n)]

def check(x,y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            if AL[i][j] == 0:
                AL[i][j] = 1
            else:
                AL[i][j] = 0



result = 0

if( n < 3 or m <3 ) and AL != BL:
    result = -1

else:
    for r in range(n-2):
        for c in range(m-2):
            if AL[r][c] != BL[r][c]:
                check(r,c)
                result += 1


if result != -1:
    if AL != BL:
        result = -1

print(result)