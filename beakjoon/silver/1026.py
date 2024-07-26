import sys
input = sys.stdin.readline

n = int(input())
s1 = list(map(int,input().split()))
s2 = list(map(int, input().split()))
result = 0

for i in range(n):

    result += min(s1)*max(s2)
    s1.pop(s1.index(min(s1)))
    s2.pop(s2.index(max(s2)))

print(result)




