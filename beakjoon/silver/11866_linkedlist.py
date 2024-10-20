import sys
input = sys.stdin.readline

n, k = map(int, input().split())
result = []

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head  # 원형 연결리스트
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head  # 마지막 노드가 다시 헤드를 가리킴

    def delete(self, node):
        if self.head is None:  # 빈 리스트 처리
            return None

        current = self.head
        prev = self.tail

        # 노드가 한 개만 있는 경우
        if current == node and current.next == self.head:
            self.head = None
            self.tail = None
            return current

        while current != node:
            prev = current
            current = current.next

        # 삭제할 노드가 head인 경우
        if current == self.head:
            self.head = self.head.next
            self.tail.next = self.head

        # 삭제할 노드가 tail인 경우
        if current == self.tail:
            self.tail = prev
            self.tail.next = self.head

        # 중간 노드 삭제
        prev.next = current.next
        return current

# 원형 연결리스트 생성 및 초기화
llst = CircularLinkedList()
for i in range(1, n + 1):
    llst.append(i)

# 요세푸스 문제 해결
current = llst.head
while len(result) < n:
    # k번째 노드를 찾음
    for _ in range(k - 1):
        current = current.next

    # 현재 노드를 삭제하고 결과에 추가
    result.append(current.data)
    current = llst.delete(current).next  # 삭제 후 다음 노드로 이동

# 결과 출력
print("<" + ', '.join(map(str, result)) + ">")
