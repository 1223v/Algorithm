import sys
input = sys.stdin.readline

N = int(input())
s = sorted(list(map(int,input().split())))

min_value = abs(s[len(s)-1] + s[0])
start = 0
end = len(s)-1

result = [s[0],s[len(s)-1]]

while start < end:

    tmp = s[end] + s[start]
    if min_value > abs(tmp):
        min_value = abs(tmp)
        result[0] = s[start]
        result[1] = s[end]
        if abs(tmp) == 0:
            break


    elif tmp < 0:
        start += 1

    elif tmp > 0:
        end -= 1

print(result[0],result[1])
