import sys
input = sys.stdin.readline

S = input().rstrip()
a = S.count('a')

K = S + S

min_value = float('inf')
for i in range(len(S)):
    min_value = min(min_value,K[i:i+a].count('b'))

print(min_value)
