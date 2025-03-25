import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

S = input().rstrip()
M = int(input())

s_lst = []
score = [-float('inf') for _ in range(len(S))]
for _ in range(M):
    tmp, score1 = map(str,input().split())

    s_lst.append([tmp,int(score1)])


def solution(start):
    global score

    if start >= len(S):
        return 0

    if score[start] != -float('inf'):
        return score[start]

    score[start] = solution(start + 1) + 1

    for k, v in s_lst:
        if S[start:start+len(k)] == k:
            score[start] = max(score[start], solution(start + len(k)) + v)

    return score[start]

print(solution(0))
