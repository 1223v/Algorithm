import sys
input = sys.stdin.readline

# N = int(input())
# A = set(map(int,input().split()))
# M= int(input())
# B = list(map(int, input().split()))
#
#
#
# for i in B:
#     if i in A:
#         print(1)
#     else:
#         print(0)

n = int(input())
A = list(map(int,input().split()))
A.sort()
M = int(input())
target_list = list(map(int,input().split()))

for i in range(M):
    find = False
    target = target_list[i]
    # 이진 탐색 시작
    start = 0
    end = len(A) - 1
    while start <= end:
        midi = int((start + end) / 2)
        midv = A[midi]
        if midv > target:
            end = midi -1
        elif midv < target:
            start = midi +1
        else:
            find = True
            break

    if find:
        print(1)
    else:
        print(0)

