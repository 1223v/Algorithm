import sys
input = sys.stdin.readline

N = int(input())
s = sorted(list(map(int,input().split())))

start = 0
end = N-1

left = start
right = end
min_value = abs(s[start] + s[end])

while start < end:

    if abs(s[start] + s[end]) < min_value:
        left = start
        right = end
        min_value = abs(s[start] + s[end])
        if min_value == 0:
            break

    if s[start] + s[end] < 0:
        start += 1
    else:
        end -= 1

print(s[left], s[right])