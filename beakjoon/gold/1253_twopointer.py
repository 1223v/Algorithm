import sys
input = sys.stdin.readline

N = int(input())
s = sorted(list(map(int,input().split())))

count = 0
for i in range(N):
    start = 0
    end = N-1
    target = s[i]

    while start < end:

        if s[start] + s[end] < target:
            start += 1

        elif s[start] + s[end] > target:
            end -= 1

        else:
            if start != i and end != i: # 서로 다 다른수여야 좋은수
                count += 1
                break

            elif start == i:
                start += 1

            elif end == i:
                end -= 1

print(count)