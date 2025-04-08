def solution(n, computers):


    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:

                graph[i].append(j)




    visited = [False] * n
    def dfs(v):
        nonlocal answer
        visited[v] = True

        for i in graph[v]:
            if not visited[i]:

                dfs(i)

    answer = 0
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)


    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))