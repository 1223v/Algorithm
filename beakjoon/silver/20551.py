import sys
input = sys.stdin.readline

N,M = map(int,input().split())
s = sorted([int(input().rstrip()) for _ in range(N)])
D = [int(input().rstrip()) for _ in range(M)]
result = []
for i in D:
    start = 0
    end = N-1
    index = N-1
    while start <= end:
        mid = (start + end) //2

        if s[mid] < i:
            start = mid + 1

        elif s[mid] == i:
            index = min(mid,index)
            end = mid -1
        else:
            end = mid-1

    if s[index] == i:
        result.append(index)
    else:
        result.append(-1)
print('\n'.join(map(str, result)))
