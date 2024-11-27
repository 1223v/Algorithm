class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# 트리 구조 생성
root = TreeNode('A')
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')
F = TreeNode('F')
G = TreeNode('G')
H = TreeNode('H')
I = TreeNode('I')

root.add_child(B)
root.add_child(C)
root.add_child(D)
C.add_child(E)
C.add_child(F)
C.add_child(G)
E.add_child(H)
E.add_child(I)

# Inorder 방식 출력 함수 (일반 트리)
def inorder(node):
    if node is None:
        return
    # 자식이 있으면 첫 번째 자식을 왼쪽으로 간주
    if node.children:
        inorder(node.children[0])  # 첫 번째 자식
    # 현재 노드 출력
    print(node.value, end=' ')
    # 나머지 자식들을 오른쪽으로 간주하고 순회
    for child in node.children[1:]:
        inorder(child)

# 트리 구조 출력 (Inorder)
print("Inorder 방식으로 출력:")
inorder(root)
