import sys
input = sys.stdin.readline

n = int(input())
result = 0
for _ in range(n):
    s = input()
    lst = [s[0]]
    for i in range(1,len(s)):

        if s[i] in lst and lst[-1] != s[i]:
            break

        lst.append(s[i])
    else:
        result += 1

print(result)