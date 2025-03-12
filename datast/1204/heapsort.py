def heapify(arr, n, i):
    largest = i  # 현재 노드를 가장 큰 값으로 가정
    l = 2 * i + 1  # 왼쪽 자식 노드
    r = 2 * i + 2  # 오른쪽 자식 노드

    # 왼쪽 자식이 존재하고, 현재 노드보다 큰 경우
    if l < n and arr[l] > arr[largest]:
        largest = l

    # 오른쪽 자식이 존재하고, 현재 largest보다 큰 경우
    if r < n and arr[r] > arr[largest]:
        largest = r

    # 가장 큰 값이 현재 노드가 아닌 경우 교환 후 재귀 호출
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 교환
        heapify(arr, n, largest)  # 재귀적으로 heapify 호출

def heapSort(arr):
    n = len(arr)

    # 힙 구성
    for i in range(n // 2 - 1, -1, -1):  # 마지막 부모 노드부터 힙 구성
        heapify(arr, n, i)

    # 힙 정렬
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 최댓값(루트)을 배열 끝으로 이동
        heapify(arr, i, 0)  # 남은 배열로 힙 구성

# 예제 데이터
data = [12, 11, 13, 5, 6, 7]
print("정렬 전:", data)

heapSort(data)
print("정렬 후:", data)
