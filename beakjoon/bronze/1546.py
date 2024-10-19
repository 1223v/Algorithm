import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int,input().split()))

max_subject = max(s)
for i in range(n):
    s[i] = s[i] / max_subject * 100

print(sum(s) / len(s))