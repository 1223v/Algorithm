
def sequential_search(A, key, low, high):
    # low부터 high까지 순차적으로 탐색
    for i in range(low, high + 1):
        # key와 일치하는 요소를 찾으면 인덱스 반환
        if A[i].key == key:
            return i
    # 찾지 못하면 None 반환
    return None


class Element:
    def __init__(self, key):
        self.key = key

# 리스트와 객체 생성
A = [Element(10), Element(20), Element(30), Element(40), Element(50)]

# 찾을 값과 범위 설정
key = 30
low = 0
high = len(A) - 1

# 순차 탐색 수행
result = sequential_search(A, key, low, high)

if result is not None:
    print(f"Element found at index: {result}")
else:
    print("Element not found.")
