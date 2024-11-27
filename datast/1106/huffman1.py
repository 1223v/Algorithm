import heapq

# 노드를 표현하기 위한 클래스
class Node:
    def __init__(self, freq, char=None):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None

    # 힙큐에서 우선순위로 사용될 수 있도록 less than 비교 연산자 정의
    def __lt__(self, other):
        return self.freq < other.freq

# 허프만 트리 구축
def build_huffman_tree(frequencies):
    heap = [Node(freq, char) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

# 허프만 코드 생성
def generate_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.char is not None:  # 리프 노드
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

# 주어진 문자 빈도
frequencies = {'A': 46, 'B': 13, 'C': 20, 'D': 10, 'E': 5, 'F': 6}

# 허프만 트리 생성
root = build_huffman_tree(frequencies)

# 허프만 코드 생성
huffman_codes = generate_codes(root)

# 결과 출력
print("허프만 코드:")
for char, code in huffman_codes.items():
    print(f"{char}: {code}")
