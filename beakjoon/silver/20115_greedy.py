import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int,input().split()))
s.sort(reverse=True)

result = s[0]
for i in range(1,n):
    result += s[i]/2


print(result)