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

def make_tree(freq):
    heap = [0]  # 힙 초기화
    for n in freq:
        heappush(heap, n)  # 빈도 수를 힙에 추가

    for i in range(1, len(freq)):
        e1 = heappop(heap)
        e2 = heappop(heap)
        heappush(heap, e1 + e2)
        print("(%d+%d)" % (e1, e2))  # 두 최소 빈도 수의 합을 출력

# 데이터 예제
label = ['E', 'T', 'N', 'I', 'S']
freq = [15, 12, 8, 6, 4]

make_tree(freq)
