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

# 트리의 높이를 계산하는 함수
def calc_height(node):
    if node is None:
        return 0
    # 각 자식 노드의 높이를 계산하여 최대값에 1을 더함
    max_height = 0
    for child in node.children:
        child_height = calc_height(child)
        if child_height > max_height:
            max_height = child_height
    return max_height + 1

# 트리의 높이 출력
print("트리의 높이:", calc_height(root))
