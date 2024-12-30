import sys
input = sys.stdin.readline

N = int(input())
s = list(map(int,input().split()))


start = 0
end = len(s)-1

first_tmp = abs(s[start] + s[end])
left_idx = start
right_idx = end

while start < end:

    tmp = s[start] + s[end]

    if abs(tmp) < first_tmp:
        left_idx=start
        right_idx = end
        first_tmp = abs(tmp)

        if first_tmp == 0:
            break

    if tmp < 0:
        start += 1

    else:
        end -= 1

print(s[left_idx],s[right_idx])
