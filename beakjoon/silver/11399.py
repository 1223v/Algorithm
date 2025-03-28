#
# N = int(input())
# A = list(map(int,input().split()))
# S = [0]*N
#
# #삽입정렬
# for i in range(1, N):
#     insert_point = i
#     insert_value = A[i]
#     for j in range(i-1, -1, -1):
#         if A[j] < A[i]:
#             insert_point = j+1
#             break
#         if j == 0:
#             insert_point = 0
#
#     for j in range(i, insert_point, -1):
#         A[j] = A[j-1]
#     #삽입 위치에 insert_value 넣어주기
#     A[insert_point] = insert_value
#
# #합배열
# S[0] = A[0]
# for i in range(1,N):
#     S[i] = S[i-1] + A[i]
#
# sum = 0
# for i in range(0,N):
#     sum += S[i]
#
# print(sum)

# 코드 줄여보기

import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

S = [0] * N

A.sort()

S[0] = A[0]
for i in range(1,N):
    S[i] = S[i-1] + A[i]

print(sum(S))