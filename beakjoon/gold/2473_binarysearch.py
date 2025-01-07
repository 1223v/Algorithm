import sys
input = sys.stdin.readline

N = int(input())
s = sorted(list(map(int,input().split())))
start,end,center = 1,N-1,0
right = end
left = start
tmp1 = float('inf')
for i in range(N-2):

    start = i + 1
    end = N-1


    while start < end:

        tmp2 = s[start] + s[end] + s[i]

        if abs(tmp2) < tmp1:

            right = end
            left = start
            center = i
            tmp1 = abs(tmp2)
            if tmp1 == 0:
                break

        if tmp2 < 0:
            start += 1
        else:
            end -= 1
# 0 (1 ~ N )
# 1 (2 ~ N)
# 2 (3 ~ N)
print(s[center],s[left],s[right])

