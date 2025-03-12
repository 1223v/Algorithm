# 병합 함수: 두 리스트를 정렬하여 병합
def merge(left, right):
    result = []  # 결과를 저장할 리스트
    i = j = 0  # 각 리스트의 포인터 초기화

    # 두 리스트를 비교하여 작은 값을 결과 리스트에 추가
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남아있는 요소를 결과 리스트에 추가
    result += left[i:]
    result += right[j:]

    return result

# 병합 정렬 함수
def merge_sort(Data):
    if len(Data) <= 1:  # 리스트 크기가 1 이하인 경우 반환
        return Data

    mid = len(Data) // 2  # 중간점 계산
    left = Data[:mid]  # 왼쪽 부분 리스트
    right = Data[mid:]  # 오른쪽 부분 리스트

    # 재귀적으로 분할하여 병합 정렬 수행
    left = merge_sort(left)
    right = merge_sort(right)

    # 정렬된 두 리스트 병합
    return merge(left, right)

# 예제 데이터
data = [38, 27, 43, 3, 9, 82, 10]
print("정렬 전:", data)

# 병합 정렬 실행
sorted_data = merge_sort(data)
print("정렬 후:", sorted_data)
