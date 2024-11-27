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

# Preorder 방식 출력 함수
def preorder(node):
    if node is None:
        return
    # 현재 노드 출력
    print(node.value, end=' ')
    # 자식 노드들을 순서대로 방문
    for child in node.children:
        preorder(child)

# 트리 구조 출력 (Preorder)
print("Preorder 방식으로 출력:")
preorder(root)
