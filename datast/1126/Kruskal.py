# 부모 테이블 초기화
parent = []

# 부모를 찾는 함수 (경로 압축 적용)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

# 두 집합을 합치는 함수 (Union by Rank)
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# Kruskal 알고리즘 구현
def kruskal(v, edges):
    global parent
    parent = [i for i in range(v)]  # 부모 초기화
    edges.sort()  # 간선들을 비용 순으로 정렬

    result = 0  # 최소 비용 신장 트리의 총 비용
    mst = []    # 최소 신장 트리에 포함된 간선 리스트

    for edge in edges:
        cost, a, b = edge
        # 두 정점이 사이클을 이루지 않는 경우에만 추가
        if find(a) != find(b):
            union(a, b)
            result += cost
            mst.append((a, b, cost))  # 최소 신장 트리에 추가

    return result, mst

# 입력: 정점의 수와 간선 리스트
v = 7  # 정점의 개수 (A, B, C, D, E, F, G)
edges = [
    (29, 0, 1),  # (가중치, 정점1, 정점2)
    (10, 0, 5),
    (16, 1, 2),
    (15, 1, 6),
    (12, 2, 3),
    (18, 3, 6),
    (22, 3, 4),
    (27, 4, 5),
    (25, 4, 6),
]

# Kruskal 알고리즘 실행
result, mst = kruskal(v, edges)

# 결과 출력
print("최소 비용:", result)
print("최소 신장 트리의 간선:")
for edge in mst:
    print(f"정점 {edge[0]} - 정점 {edge[1]} (비용: {edge[2]})")
