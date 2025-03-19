import sys
input = sys.stdin.readline

N,M = map(int,input().split())

graph = []
for i in range(N):
    S = list(map(int, input().split()))
    for x in S:
        graph.append((x,i))


graph.sort()
min_value = float('inf')

start = 0
end = 2
while start < end:

    if end > len(graph):
        break

    if graph[end][1] == graph[start][1]:






print(graph)