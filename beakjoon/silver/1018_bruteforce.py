# # 다시 풀어볼 문제
# import sys
# input = sys.stdin.readline
#
# N,M = map(int,input().split())
#
# s = [input().rstrip() for _ in range(N)]
#
# result = []
# for a in range(N-7):
#     for b in range(M-7):
#         w1 = 0
#         B2 = 0
#         for i in range(a, a+8):
#             for j in range(b, b+8):
#                 if (i+j) % 2 == 0:
#                     if s[i][j] == "B":
#                         B2 += 1
#                     if s[i][j] == "W":
#                         w1 += 1
#                 else:
#                     if s[i][j] == "B":
#                         w1 += 1
#                     if s[i][j] == "W":
#                         B2 += 1
#
#
#         result.append(min(w1,B2))
# print(min(result))

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
s = [input().rstrip() for _ in range(N)]

result = []

w_board = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
]

b_board = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
]
def check(i,j):
    result_w = 0
    result_b = 0
    for di in range(8):
        for dj in range(8):
            ni,nj = i+di, j+dj
            if s[ni][nj] != w_board[di][dj]:
                result_w += 1
            if s[ni][nj] != b_board[di][dj]:
                result_b += 1
    return min(result_w, result_b)

for a in range(N-7):
    for b in range(M-7):
        result.append(check(a,b))

print(min(result))

