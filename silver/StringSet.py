import sys

# n, m = map(int, sys.stdin.readline().split())
#
# correct_sentences = [(sys.stdin.readline().rstrip()) for _ in range(n)]
# problem_sentences = [(sys.stdin.readline().rstrip()) for _ in range(m)]
# print(correct_sentences)
# cnt = 0
# for i in problem_sentences:
#     if i in correct_sentences:
#         cnt +=1
#
# print(cnt)

# n, m = map(int,input().split())
# s= set([input() for _ in range(n)])
# cnt = 0
# print(s)
# for _ in range(m):
#     t = input().rstrip()
#     if t in s:
#         cnt += 1
#
# print(cnt)a           

n, m = map(int,input().split())

d= dict()
cnt = 0

for _ in range(n):
    s = input().rstrip()
    d[s] = 1

for i in range(m):
    t = input().rstrip()
    if t in d:
        cnt +=1
print(cnt)