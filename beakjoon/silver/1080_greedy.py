import sys
input = sys.stdin.readline

N, M = map(int,input().split())

s1 = [list(map(int,input().rstrip())) for _ in range(N)]
s2 = [list(map(int,input().rstrip())) for _ in range(N)]

cnt = 0
if (N<3 or M < 3) and s1 != s2:
    cnt = -1

else:
    for i in range(N-2):
        for j in range(M-2):
            if s1[i][j] != s2[i][j]:
                for x in range(i,i+3):
                    for y in range(j, j+3):
                        if s1[x][y] == 1:
                            s1[x][y] = 0
                        else:
                            s1[x][y] = 1

                cnt += 1

if cnt != -1:
    if s1 != s2:
        print(-1)
        exit()

print(cnt)
