import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()
max_value = 0
stu_lst=[]
for _ in range(N):
    s = input()
    tmp = s.split()
    k1 = int(tmp[0])
    if k1 == 1:
        k2 = int(tmp[1])
        queue.append(k2)
        if max_value < len(queue):
            stu_lst = []
            stu_lst.append(k2)
            max_value = len(queue)
        elif max_value == len(queue):
            stu_lst.append(k2)

    else:
        queue.popleft()

stu_lst.sort()
print(max_value,stu_lst[0])