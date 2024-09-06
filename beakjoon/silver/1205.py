import sys
input = sys.stdin.readline

n,new, p = map(int,input().split())
score = list(map(int, input().split()))

if n == 0:
    print(1)

else:
    if n==p and score[-1] >= new:
        print(-1)

    else:
        res = n+1
        for i in range(n):
            if score[i] <= new:
                res = i+1
                break

        print(res)