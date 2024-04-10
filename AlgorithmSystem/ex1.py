from collections import defaultdict


def dfs(graph, node, intervals, start, parent):
    # 현재 노드에 대한 시작 지점을 할당
    intervals[node] = [start, start]
    # 현재 노드의 모든 자식을 DFS로 탐색
    for child in graph[node]:
        if child != parent:  # 부모 노드를 다시 방문하지 않도록 함
            # 자식 노드에 대해 DFS 탐색을 계속하며, 시작 지점을 1 증가시킴
            intervals[node][1] = dfs(graph, child, intervals, start + 1, node)
            start = intervals[node][1]
    # 현재 노드의 종료 지점을 반환
    return intervals[node][1] + 1


def tree_to_interval(n, edges):
    # 그래프 초기화
    graph = defaultdict(list)
    # 에지 정보를 사용하여 양방향 그래프 생성
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # 각 정점에 대한 구간을 저장할 딕셔너리
    intervals = {}
    # DFS를 사용하여 구간 찾기 (1번 노드부터 시작)
    dfs(graph, 1, intervals, 0, -1)

    # 출력 형식에 맞춰 정렬 및 반환
    result = [intervals[i] for i in range(1, n + 1)]
    return result


# 예제 입력
n = 3
edges = [(3, 2), (1, 2)]

# 트리를 구간 그래프로 변환
intervals = tree_to_interval(n, edges)

# 출력 확인
print(intervals)
