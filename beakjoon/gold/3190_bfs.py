import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
K = int(input())
alst = [tuple(map(int,input().split())) for _ in range(K)]

dtbl = [0] * (10001)
L = int(input())

for _ in range(L):
    sec, turn = map(str,input().split())
    dtbl[int(sec)] = turn

di = [-1,0,1,0]
dj = [0,1,0,-1]

snake = deque([(1,1)])
dr = 1
result_time = 0


while True:

    ci, cj = snake[-1]
    ni,nj = ci+di[dr], cj+dj[dr]
    if 1 <= ni <= N and 1 <= nj <= N and (ni,nj) not in snake: # 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
        snake.append((ni,nj)) # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
        result_time += 1
        # 사과 먹기
        if (ni,nj) in alst: # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
            alst.remove((ni,nj))
        else: # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
            snake.popleft()

        if dtbl[result_time] == "D":
            dr = (dr+1) % 4
        elif dtbl[result_time] == "L":
            dr = (dr + 3) % 4

    else:

        break

print(result_time+1)
