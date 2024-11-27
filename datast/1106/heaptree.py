def heappush(heap, n):
    heap.append(n)
    i = len(heap) - 1
    while i != 1:
        pi = i // 2
        if n <= heap[pi]:
            break
        heap[i] = heap[pi]
        i = pi
    heap[i] = n

def heappop(heap):
    size = len(heap) - 1
    if size == 0:
        return None
    pi = 1
    i = 2
    root = heap[1]
    last = heap[size]
    while i <= size:
        if i < size and heap[i] < heap[i + 1]:
            i += 1
        if last >= heap[i]:
            break
        heap[pi] = heap[i]
        pi = i
        i *= 2
    heap[pi] = last
    heap.pop()
    return root

# 초기 리스트
data = [8, 5, 7, 3, 2, 3, 4]

# 힙 초기화 (인덱스 0은 사용하지 않음)
heap = [None]

# 모든 요소를 힙에 삽입
for value in data:
    heappush(heap, value)

# 모든 요소를 힙에서 제거하여 내림차순으로 정렬
sorted_result = []
while len(heap) > 1:  # 힙에 요소가 있을 때까지
    sorted_result.append(heappop(heap))

print(sorted_result)
