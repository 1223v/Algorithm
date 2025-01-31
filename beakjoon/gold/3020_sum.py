import sys
input = sys.stdin.readline

N, H = map(int,input().split())
graph = [0] * (H)
for i in range(N):
    B = int(input())

    if i % 2 == 0:
        graph[0] += 1
        graph[B] -= 1

    else:
        graph[H-B] += 1

for i in range(1,H):
    graph[i] += graph[i-1]

min_value = min(graph)
print(min_value, graph.count(min_value))