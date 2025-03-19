import sys
input = sys.stdin.readline

N, K, T = map(int,input().split())

A = sorted(list(map(int,input().split())))

start = 0
end = len(A) - 1
count = 0
while start < end:

    if A[start] == 0:
        start += 1
        continue

    elif A[end] == K:
        end -= 1
        continue

    move = min(A[start], K-A[end])
    A[start] -= move
    A[end] += move

    count += move

    if count > T:
        print("NO")
        exit()


if all(x== 0 or x== K for x in A):
    print("YES")

else:
    print("NO")
