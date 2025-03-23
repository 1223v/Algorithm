import sys
input = sys.stdin.readline

N,K,T = map(int,input().split())
graph = sorted(list(map(int,input().split())))

cnt = 0
start = 0
end = N-1
while start < end:


    if cnt > T:

        print("NO")
        exit()

    if graph[start] == 0:

        start += 1

    if graph[end] == K:

        end -= 1


    if start < end and graph[start]!=0 and graph[end]!=K:
        if graph[start] + graph[end] < K:

            graph[end] += graph[start]
            cnt += graph[start]

            graph[start] = 0


        elif graph[start] + graph[end] >= K:

            tmp = K - graph[end]
            graph[start] -= tmp
            cnt += tmp

            graph[end] = K



if all(i ==0 or i ==K for i in graph):
    print("YES")

else:

    print("NO")
