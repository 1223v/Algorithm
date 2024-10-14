import sys
input = sys.stdin.readline

s = input().rstrip()

result = []

for i in range(len(s)):
    tmp = s[i:]
    result.append(tmp)

print('\n'.join(sorted(result)))


