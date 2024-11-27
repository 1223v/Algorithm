class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# 트리 구조 생성
root = TreeNode('A')  # 루트 노드
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')
F = TreeNode('F')
G = TreeNode('G')
H = TreeNode('H')
I = TreeNode('I')

# 트리 노드 연결
root.add_child(B)
root.add_child(C)
root.add_child(D)
C.add_child(E)
C.add_child(F)
C.add_child(G)
E.add_child(H)
E.add_child(I)

# 트리 구조 출력 (수동으로 확인 가능)
print("트리 구조:")
print(f"{root.value}의 자식들: {[child.value for child in root.children]}")
print(f"{C.value}의 자식들: {[child.value for child in C.children]}")
print(f"{E.value}의 자식들: {[child.value for child in E.children]}")
print(f"{F.value}의 자식들: {[child.value for child in F.children]}")  # F는 자식이 없음
