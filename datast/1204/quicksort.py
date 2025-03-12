# Partition 함수 정의
def partition(Data, left, right):
    wherePivot = left  # 피벗을 배열의 첫 번째 요소로 설정
    pivot = Data[wherePivot]

    while left < right:
        # 왼쪽 포인터를 오른쪽으로 이동
        while left < len(Data) and Data[left] <= pivot:
            left += 1
        # 오른쪽 포인터를 왼쪽으로 이동
        while Data[right] > pivot:
            right -= 1

        # 두 포인터가 교차하지 않았다면 스왑
        if left < right:
            Data[left], Data[right] = Data[right], Data[left]

    # 피벗과 최종 위치의 요소를 스왑
    Data[wherePivot], Data[right] = Data[right], Data[wherePivot]
    return right  # 피벗의 최종 위치 반환

# Quick Sort 함수 정의
def quick_sort(Data, i, j):
    if i < j:
        pivot = partition(Data, i, j)  # 피벗 구하기
        quick_sort(Data, i, pivot - 1)  # 피벗 왼쪽 부분 정렬
        quick_sort(Data, pivot + 1, j)  # 피벗 오른쪽 부분 정렬

# 예제 데이터
data = [29, 10, 14, 37, 13]
print("정렬 전:", data)

# 퀵 정렬 실행
quick_sort(data, 0, len(data) - 1)
print("정렬 후:", data)
