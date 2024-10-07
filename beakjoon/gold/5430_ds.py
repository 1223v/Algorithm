import sys
from collections import deque
input = sys.stdin.readline

n = int(input())



for _ in range(n):
    command = input().rstrip()
    slength = int(input())
    queue = deque(input().rstrip()[1:-1].split(","))

    if slength == 0:
        queue=[]

    error_flag = False  # 에러 발생 여부 플래그
    rev = 0
    for i in command:

        if i == 'R':
            rev += 1
        elif i == 'D':
            if len(queue) < 1:  # 덱이 비어있지 않은 경우
                error_flag = True
                print("error")
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()


    if not error_flag:
        if rev % 2 == 0:

            print('['+','.join(queue) + "]")
        else:
            queue.reverse()
            print('['+','.join(queue) + "]")


