from collections import defaultdict, deque


def tree_levels(V, edges):
    # Step 1: 트리 구성
    tree = defaultdict(list)
    for i in range(0, len(edges), 2):
        parent, child = edges[i], edges[i + 1]
        tree[parent].append(child)

    # Step 2: BFS를 통해 각 레벨의 노드를 찾기
    result = []
    queue = deque([1])  # 루트 노드에서 시작
    while queue:
        level_size = len(queue)
        level_nodes = []

        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node)
            # 현재 노드의 자식을 큐에 추가
            for child in tree[node]:
                queue.append(child)

        result.append(level_nodes)

    # Step 3: 원하는 형식으로 결과 출력
    for level in result:
        print(" ".join(map(str, level)))


# 예시 입력
V = 13
edges = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

tree_levels(V, edges)
