import sys
input = sys.stdin.readline
s = [1] + [0] * 30
# s = [int(input()) for i in range(28)]
# s.sort()
# tmp = 1
#
# for i in range(28):
#
#     if s[i] != tmp:
#         print(tmp)
#         tmp += 1
#     tmp += 1
#
# while tmp <= 30:
#     print(tmp)
#     tmp += 1

for i in range(1,29):
    a = int(input())
    s[a] = 1

print([i for i, value in enumerate(s) if value == 0])
