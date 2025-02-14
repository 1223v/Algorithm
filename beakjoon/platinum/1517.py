import sys
input = sys.stdin.readline

result = 0

def merge_sort(start,end):
    global result

    if end - start < 1:
        return

    mid = int((start + end)/2)
    merge_sort(start,mid)
    merge_sort(mid + 1, end)

    for i in range(start, end + 1):
        tmp[i] = s[i]

    k = start
    index1 = start
    index2 = mid + 1

    while index1 <= mid and index2 <= end:

        if tmp[index1] > tmp[index2]:
            s[k] = tmp[index2]
            result += index2 - k
            k += 1
            index2 += 1

        else:
            s[k] = tmp[index1]
            k += 1
            index1 += 1

    while index1 <= mid:
        s[k] = tmp[index1]
        k += 1
        index1 += 1

    while index2 <= end:
        s[k] = tmp[index2]
        k += 1
        index2 += 1


N = int(input())
s = list(map(int,input().split()))
s.insert(0,0)
tmp = [0] * (N+1)
merge_sort(1,N)
print(result)