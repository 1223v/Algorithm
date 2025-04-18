import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()
for _ in range(N):
    s = input().rstrip()
    lst_s = s.split()


    if lst_s[0] == "push":

        queue.append(lst_s[1])


    elif lst_s[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif lst_s[0] == "size":
        print(len(queue))

    elif lst_s[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)

    elif lst_s[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif lst_s[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)

