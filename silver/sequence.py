import sys

# [1, 2, 3], 4, 5 (처음 위치)
# 1, [2, 3, 4], 5
# 1, 2, [3, 4, 5] (마지막 위치)

n, m = map(int,sys.stdin.readline().split())
seq_list = list(map(int, sys.stdin.readline().split()))
# 첫 번째 윈도우의 합을 계산
current_sum = sum(seq_list[:m])
max_sum = current_sum

# 슬라이딩 윈도우를 이용해 각 윈도우의 합을 계산
for i in range(1, n-m+1):
    current_sum = current_sum - seq_list[i - 1] + seq_list[i+m-1]
    max_sum= max(max_sum, current_sum)

print(max_sum)
