from collections import defaultdict
#간선 목록을 입력으로 받음
edges = [(4, 1), (3, 1), (2, 1), (5, 1), (5, 6)]

# 그래프 클래스를 사용하지 않고, 간선 목록에서 바로 인터벌 그래프 여부를 판단하는 함수를 구현
def interval_graph_check(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = {}
    start = {}
    finish = {}
    time = 0

    print(graph)
    def dfs(v,m):
        nonlocal time
        print("return", m, graph[v], v)
        if m in graph[v] or m == v:
            visited[v] = True
            time += 1
            start[v] = time
            for i in graph[v]:
                if i not in visited:
                    print("재귀 호출", i)
                    dfs(i,m)

            time +=v
            finish[v] = time
            time += 1
        else:

            return

    # 모든 노드에 대해 DFS 실행
    for v in graph:

        if v not in visited:
            print("리턴!!!!!!!!!!!!!!!!!!!!!!!!!", time)
            dfs(v,v)

    # 인터벌 그래프 판별 로직
    intervals = [(start[v], finish[v]) for v in start]
    print(intervals)
    # 각 인터벌을 끝나는 시간 기준으로 정렬
    intervals.sort(key=lambda x: x[1])

    # 인접한 인터벌이 정점의 인접 관계를 정확히 반영하는지 검사
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:  # 인접한 인터벌이 겹치면
            # 인접 리스트에서 실제로 인접한지 확인
            overlap = False
            for v in graph:
                if start[v] == intervals[i - 1][0] and finish[v] == intervals[i - 1][1]:
                    for u in graph[v]:
                        if start[u] == intervals[i][0] and finish[u] == intervals[i][1]:
                            overlap = True
                            break
                if overlap:
                    break
            if not overlap:  # 겹치지만 인접 리스트에 없으면 인터벌 그래프가 아님
                return -1
    return 1


# 주어진 간선 목록으로 인터벌 그래프 여부 판단
result = interval_graph_check(edges)
print(result)