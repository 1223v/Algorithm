class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.val:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def print_level_order(root): # 레벨 별로 트리 출력
    if not root:
        return
    queue = [root] # 현재 레벨의 모든 노드를 담을 큐
    level_number = 1 # 현재 레벨 번호
    while queue:
        level_size = len(queue) # 현재 레벨에 있는 노드 수
        print("레벨 %d: " % level_number, end="")
        while level_size > 0:
            node = queue.pop(0) # 큐에서 노드 제거
            print("%d" % node.val, end=" ") # 노드 값을 출력하고 , 공백을 출력
            # 왼쪽, 오른쪽 자식 노드가 있으면
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            level_size -= 1
        print() # 현재 레벨 출력 후 줄바꿈
        level_number += 1 # 레벨 번호 증가


# 숫자 배열 정의
nums = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
root = None
for num in nums:
    root = insert(root,num) # 트리에 숫자 삽입
    print("'%d' 삽입 후 트리:" %num)
    print_level_order(root) # 현재 틀리의 레벨별 출력
    print() # 출력 간 구분을 위해 빈줄 추가
