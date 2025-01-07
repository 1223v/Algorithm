# 톱니바퀴를 K 번째 회전
# 회전 방향은 시계, 반시계
# 극이 다른 경우 돌린 방향의 반대 방향으로 돌아감

# 1번 => 12시 N 0 S 1
# 2번 => 12시 N 0 S 2
# 3번 => 12시 N 0 S 4
# 4번 => 12시 N 0 S 8

import sys
input = sys.stdin.readline

s = [list(map(int,input().rstrip())) for _ in range(4)]
K = int(input()) # 회전 횟수
dire_lst = [[1,-1,1,-1],[-1,1,-1,1]]

result_lst = []
for _ in range(K):
    s_num, direction = map(int,input().split()) # 톱니바퀴 번호, 방향 (1 : 시계 방향, -1 : 반시계 방향)
    chk1, chk2, chk3, chk4 = False, False, False, False
    tmp0,tmp1,tmp2,tmp3 = [],[],[],[]

    if dire_lst[0][s_num-1] == direction:
        if s_num == 1:

            tmp0 = [s[0][7]] + s[0][0:7]
            if s[0][2] != s[1][6]:
                chk1 = True
                tmp1 = s[1][1:] + [s[1][0]]

            if s[1][2] != s[2][6] and chk1:
                chk2 = True
                tmp2 = [s[2][7]] + s[2][0:7]

            if s[2][2] != s[3][6] and chk2:
                tmp3 = s[3][1:] + [s[3][0]]

        elif s_num == 2:
            tmp1 = s[1][1:] + [s[1][0]]
            if s[1][6] != s[0][2]:
                tmp0 = [s[0][7]] + s[0][0:7]

            if s[1][2] != s[2][6]:
                chk2 = True
                tmp2 = [s[2][7]] + s[2][0:7]

            if s[2][2] != s[3][6] and chk2:
                tmp3 = s[3][1:] + [s[3][0]]


        elif s_num == 3:
            tmp2 = [s[2][7]] + s[2][0:7]

            if s[2][2] != s[3][6]:
                tmp3 = s[3][1:] + [s[3][0]]

            if s[1][2] != s[2][6]:
                chk2 = True
                tmp1 = s[1][1:] + [s[1][0]]

            if s[1][6] != s[0][2] and chk2:
                tmp0 = [s[0][7]] + s[0][0:7]

        else:
            tmp3 = s[3][1:] + [s[3][0]]
            if s[2][2] != s[3][6]:
                chk3 = True
                tmp2 = [s[2][7]] + s[2][0:7]

            if s[1][2] != s[2][6] and chk3:
                chk2 = True
                tmp1 = s[1][1:] + [s[1][0]]


            if s[0][2] != s[1][6] and chk2:
                tmp0 = [s[0][7]] + s[0][0:7]

        if len(tmp0) != 0:
            s[0] = tmp0[::]
        if len(tmp1) != 0:
            s[1] = tmp1[::]
        if len(tmp2) != 0:
            s[2] = tmp2[::]
        if len(tmp3) != 0:
            s[3] = tmp3[::]

    else:
        if s_num == 1:
            tmp0 = s[0][1:] + [s[0][0]]
            if s[0][2] != s[1][6]:
                chk1 = True
                tmp1 = [s[1][7]] + s[1][0:7]

            if s[1][2] != s[2][6] and chk1:
                chk2 = True
                tmp2 = s[2][1:] + [s[2][0]]

            if s[2][2] != s[3][6] and chk2:
                tmp3 = [s[3][7]] + s[3][0:7]

        elif s_num == 2:
            tmp1 = [s[1][7]] + s[1][0:7]
            if s[1][6] != s[0][2]:
                tmp0 = s[0][1:] + [s[0][0]]

            if s[1][2] != s[2][6]:
                chk2 = True
                tmp2 = s[2][1:] + [s[2][0]]

            if s[2][2] != s[3][6] and chk2:
                tmp3 = [s[3][7]] + s[3][0:7]


        elif s_num == 3:
            tmp2 = s[2][1:] + [s[2][0]]

            if s[2][2] != s[3][6]:
                tmp3 = [s[3][7]] + s[3][0:7]

            if s[1][2] != s[2][6]:
                chk2 = True
                tmp1 = [s[1][7]] + s[1][0:7]

            if s[1][6] != s[0][2] and chk2:
                tmp0 = s[0][1:] + [s[0][0]]

        else:
            tmp3 = [s[3][7]] + s[3][0:7]
            if s[2][2] != s[3][6]:
                chk3 = True
                tmp2 = s[2][1:] + [s[2][0]]

            if s[1][2] != s[2][6] and chk3:
                chk2 = True
                tmp1 = [s[1][7]] + s[1][0:7]

            if s[0][2] != s[1][6] and chk2:
                tmp0 = s[0][1:] + [s[0][0]]

        if len(tmp0) != 0:
            s[0] = tmp0[::]
        if len(tmp1) != 0:
            s[1] = tmp1[::]
        if len(tmp2) != 0:
            s[2] = tmp2[::]
        if len(tmp3) != 0:
            s[3] = tmp3[::]




result = 0
if s[0][0] == 1:
    result += 1

if s[1][0] == 1:
    result += 2

if s[2][0] == 1:
    result += 4

if s[3][0] == 1:
    result += 8

print(result)
