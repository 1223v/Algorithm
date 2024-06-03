import sys

input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
count = 0
A.sort()

for k in range(n):
    find = A[k]
    start_index = 0
    end_index = n-1
    while start_index < end_index:
        if A[start_index] + A[end_index] < find:
            start_index += 1
        elif A[start_index] + A[end_index] > find:
            end_index -= 1
        else:
            if start_index != k and end_index != k:
                count += 1
                break
            elif start_index == k:
                start_index += 1
            elif end_index == k:
                end_index -= 1

print(count)