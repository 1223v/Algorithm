import sys
input = sys.stdin.readline

n = int(input())
A = []
for i in range(n):
    m = input().strip()
    A.append(m)

# 리스트를 정렬하고 집합으로 중복을 제거한 후, 다시 리스트로 변환하여 정렬
unique_sorted_A = sorted(set(A))

# 길이별로 문자열을 출력
for i in range(1, 51):
    for j in unique_sorted_A:
        if len(j) == i:
            print(j)