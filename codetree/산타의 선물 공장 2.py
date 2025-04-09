import sys

sys.stdin = open("input.txt", "r")
import math
from collections import defaultdict

T = int(input())

tmp = list(map(int,input().split()))

N,M = tmp[1],tmp[2]
belt = [[] for _ in range(N+1)]
pos = {}

for i in range(len(tmp)-1,2,-1):
    belt[tmp[i]].append(i-2)
    pos[i-2] = tmp[i]




# m_src -> m_dst로 모두 앞으로 옮기기. => 완성
def two_move_all(m_src,m_dst):

    if belt[m_src]:
        tmp1 = belt[m_src]

        belt[m_dst] = belt[m_dst] + tmp1

        for i in tmp1:
            pos[i] = m_dst

        belt[m_src] = []



    # print(belt)
    # print(pos)
    print(len(belt[m_dst]))


# m_src <-> m_dst 가장 앞에 있는 선물과 교체. 둘중 하나 없으면 옮기기만 함.
def three_front_move(m_src,m_dst):

    if belt[m_src] and belt[m_dst]:
        belt[m_src][-1], belt[m_dst][-1] = belt[m_dst][-1], belt[m_src][-1]
        pos[belt[m_dst][-1]] = m_src
        pos[belt[m_src][-1]] = m_dst


    elif belt[m_src]:
        x = belt[m_src].pop()
        belt[m_dst].append(x)
        pos[x] = m_dst


    elif belt[m_dst]:
        x = belt[m_dst].pop()
        belt[m_src].append(x)
        pos[x] = m_src

    # print(belt)
    # print(pos)
    print(len(belt[m_dst]))


def four_div(m_src,m_dst):
    #print(belt,m_src,m_dst)
    if len(belt[m_src]) > 1:
        #print("debug",len(belt[m_src]) -1, math.floor(len(belt[m_src])/2))
        if len(belt[m_src]) == 2:
            x = belt[m_src].pop()
            belt[m_dst].append(x)

            pos[x] = m_dst
        else:
            for i in range(len(belt[m_src]) -1, math.floor(len(belt[m_src])/2), -1):

                x = belt[m_src].pop()
                belt[m_dst].append(x)

                pos[x] = m_dst

    #print(belt)
    # print(pos)
    print(len(belt[m_dst]))


# p_num이 주어지면, 앞 뒤, a,b
def five_info_gift(p_num):
    a,b=0,0

    # 빈경우
    if not belt[pos[p_num]]:
        a,b = -1,-1

    else:
        if p_num not in belt[pos[p_num]]:
            a, b = -1, -1
        # 둘다 없는 경우(1개만 있음)
        elif belt[pos[p_num]].index(p_num) == 0 and belt[pos[p_num]].index(p_num) == len(belt[pos[p_num]]) - 1:
            a,b = -1,-1

        # 앞만 없는 경우
        elif belt[pos[p_num]].index(p_num) == 0:
            # print("debug",belt[pos[p_num]].index(p_num),p_num,belt[pos[p_num]])
            a = belt[pos[p_num]][belt[pos[p_num]].index(p_num)+1]
            b = -1

        # 뒤만 없는 경우
        elif belt[pos[p_num]].index(p_num) == len(belt[pos[p_num]]) - 1:
            a = -1
            b = belt[pos[p_num]][belt[pos[p_num]].index(p_num)-1]



        # 둘다 있는 경우
        else:
            a = belt[pos[p_num]][belt[pos[p_num]].index(p_num)+1]
            b = belt[pos[p_num]][belt[pos[p_num]].index(p_num)-1]

    # print(belt)
    # print(pos)
    # print(a,b)
    print(a+2*b)


def six_info_belt(b_num):

    if belt[b_num]:
        a = belt[b_num][-1]
        b = belt[b_num][0]
        c = len(belt[b_num])


    else:
        a,b,c = -1,-1,0

    # print(belt)
    # print(pos)
    print(a+2*b+3*c)


for i in range(1,T):

    tmp_commands = list(map(int,input().split()))

    if tmp_commands[0] == 200:
        two_move_all(tmp_commands[1],tmp_commands[2])

    elif tmp_commands[0] == 300:
        three_front_move(tmp_commands[1],tmp_commands[2])
    elif tmp_commands[0] == 400:
        four_div(tmp_commands[1],tmp_commands[2])
    elif tmp_commands[0] == 500:
        five_info_gift(tmp_commands[1])
    elif tmp_commands[0] == 600:
        six_info_belt(tmp_commands[1])





# 8
# 100 4 6 1 2 2 2 1 4
# 200 2 4
# 300 2 4
# 400 4 2
# 500 6
# 500 5
# 600 1
# 600 3