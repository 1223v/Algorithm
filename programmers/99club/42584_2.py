from collections import deque

def solutions(prices):

    queue = deque(prices)
    result = []
    while queue:
        x=queue.popleft()
        cnt = 0
        for i in queue:
            cnt += 1
            if x > i:
                break

        result.append(cnt)

    return result

print(solutions([1, 2, 3, 2, 3]))