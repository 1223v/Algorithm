# N * N 지도
# 길을 지나갈 수 있으려면 모든 칸 높이가 같아야함
# 경사로를 놓아 지나갈 수 있는 길을 만들 수 있음
# 경사로 높이는 1 길이는 L => 갯수 제한 없음
# 경사로는 낮은 칸에 배치
# 낮은 칸과 높은 칸 차이는 1
# 경사로 놓을 낮은 칸 L개의 칸이 연속
# 경사로가 겹치는 경우
# 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
# 범위를 벗어나는 경우

import sys
input = sys.stdin.readline

N, L = map(int,input().split())

field = [list(map(int,input().split())) for _ in range(N)]
result = 0
# 가로 확인
for i in range(N):
    visited = [0] * N
    for j in range(1,N):
        if visited[j] == 1: continue
        # 경사가 존재하는 경우
        if field[i][j-1] != field[i][j]:
            # 내리막인 경우
            if field[i][j - 1] > field[i][j]:

                if abs(field[i][j-1] - field[i][j]) > 1:
                    break

                if j+L > N:
                    break
                chk = False
                for k in range(j,j+L):
                    if field[i][k] != field[i][j]:
                        chk = True
                        break
                    if visited[k] == 1:
                        chk = True
                        break
                else:
                    for k in range(j,j+L):
                        visited[k] = 1

                if chk:
                    break




            # 오르막인 경우
            else:
                if abs(field[i][j - 1] - field[i][j]) > 1:
                    break

                if j - L < 0:
                    break

                chk = False
                for k in range(j-1, j-L-1,-1):
                    if k < 0:
                        chk = True
                        break
                    if field[i][k] != field[i][j-1]:
                        chk = True
                        break
                    if visited[k] == 1:
                        chk = True
                        break
                else:
                    for k in range(j-1, j-L-1,-1):
                        visited[k] = 1

                if chk:
                    break

    else:

        result += 1



# 세로 확인
for i in range(N):
    visited = [0] * N
    for j in range(1,N):
        if visited[j] == 1: continue
        # 경사가 존재하는 경우
        if field[j-1][i] != field[j][i]:

            # 내리막인 경우
            if field[j-1][i] > field[j][i]:

                if abs(field[j-1][i] - field[j][i]) > 1:
                    break

                if j+L > N:
                    break

                chk = False
                for k in range(j,j+L):
                    if field[k][i] != field[j][i]:
                        chk = True
                        break
                    if visited[k] == 1:
                        chk = True
                        break
                else:
                    for k in range(j,j+L):
                        visited[k] = 1
                if chk:
                    break

            # 오르막인 경우
            else:
                if abs(field[j - 1][i] - field[j][i]) > 1:
                    break

                if j - L < 0:
                    break

                chk = False
                for k in range(j-1, j-L-1,-1):
                    if j < 0:
                        chk = True
                        break
                    if field[k][i] != field[j-1][i]:
                        chk = True
                        break
                    if visited[k] == 1:
                        chk = True
                        break
                else:
                    for k in range(j-1, j-L-1,-1):
                        visited[k] = 1

                if chk:
                    break

    else:

        result += 1
print(result)