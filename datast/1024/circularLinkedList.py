class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head  # 원형 링크 연결
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def get_josephus_position(self, k):
        current = self.head
        # 한 명만 남을 때까지 반복
        while current.next != current:
            # k번째 노드 찾기
            for _ in range(k - 1):
                current = current.next
            # k번째 사람 제거
            print(f"{current.next.data} 제거")
            current.next = current.next.next
            current = current.next
        return current.data

# 인원 수와 제거할 간격 설정
n = 7  # 총 인원
k = 3  # 제거할 간격

# 원형 연결 리스트에 n명의 사람 추가
circle = CircularLinkedList()
for i in range(1, n + 1):
    circle.append(i)

# 마지막에 남는 사람의 위치 찾기
last_person = circle.get_josephus_position(k)
print(last_person)
