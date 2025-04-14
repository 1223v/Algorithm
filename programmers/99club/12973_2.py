from collections import deque

def solution(s):

    queue = deque()

    for i in s:

        if queue and queue[-1] == i:
            queue.pop()
        else:
            queue.append(i)

    if queue:
        return 0
    else:
        return 1


print(solution("cdcd"))