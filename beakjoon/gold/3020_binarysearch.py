import sys
input = sys.stdin.readline

N, H = map(int,input().split())
graph = [0] * (H)

for i in range(N):
    B = int(input())
    if i % 2==0:
        graph[0] += 1
        graph[B] -= 1

    else:
        graph[H-B] += 1

for i in range(1,H):
    graph[i] += graph[i-1]


graph.sort()
min_value = min(graph)

def left_bisect(target, s):
    left = 0
    right = H-1

    while left < right:
        mid = (left+right) // 2

        if s[mid] < target:
            left = mid + 1

        else:
            right = mid

    return left

def right_bisect(target, s):
    left = 0
    right = H-1

    while left < right:
        mid = (left + right) // 2

        if s[mid] <= target:
            left = mid + 1

        else:
            right = mid

    return left

min_count = right_bisect(min_value,graph)-left_bisect(min_value,graph)
print(min_value,min_count)
