from queue import Queue
import random


# 기수 정렬 함수 정의
def radix_sort(A):
    BUCKETS = 10  # 버킷 수 (0~9)
    DIGITS = 4  # 최대 자리수 (예: 4자리 숫자)

    # 버킷(큐) 초기화
    queues = [Queue() for _ in range(BUCKETS)]

    n = len(A)
    factor = 1  # 현재 자리수에 해당하는 분배 기준

    for d in range(DIGITS):  # 자릿수 반복
        # 현재 자리수에 맞게 분배
        for i in range(n):
            bucket_index = (A[i] // factor) % BUCKETS
            queues[bucket_index].put(A[i])

        # 큐에서 값을 꺼내어 배열에 재배치
        i = 0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[i] = queues[b].get()
                i += 1

        # 다음 자리수로 이동
        factor *= BUCKETS
        print(f"step {d + 1}: {A}")  # 각 단계별 배열 상태 출력


# 테스트 데이터 생성 및 정렬 실행
BUCKETS = 10
DIGITS = 4
data = [random.randint(1, 9999) for _ in range(10)]  # 랜덤 데이터 생성

print("정렬 전:", data)
radix_sort(data)
print("정렬 후:", data)
