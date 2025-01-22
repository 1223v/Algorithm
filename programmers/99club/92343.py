def solution(info, edges):

    graph = [[] for _ in range(len(info))]
    visited = [False] * (len(info))
    max_value = 1

    for s,e in edges:
        graph[s].append(e)

    def dfs(v,sheep, wolf, now_lst):
        nonlocal max_value
        if sheep <= wolf or not now_lst:
            return

        now_lst = graph[v] + now_lst


        for i in now_lst:
            if not visited[i]:
                visited[i] = True
                if info[i] == 0:
                    dfs(i,sheep+1,wolf,now_lst)

                else:
                    dfs(i,sheep,wolf+1,now_lst)
                visited[i] = False

        max_value = max(max_value, sheep)

    visited[0] = True
    dfs(0,1,0,[0])

    return max_value


print(solution([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))
