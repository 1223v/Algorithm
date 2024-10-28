# https://www.acmicpc.net/problem/1072
import sys
input = sys.stdin.readline

X, Y = map(int,input().split())
check = (Y * 100) // X
start = 0
end = X
result = X
if check>=99:
  print(-1)

else:
    while start <= end:
        middle = (start+end)//2

        if (100 * (Y+middle)) // (X+middle) > check:
            result = middle
            end = middle - 1

        else:
            start = middle + 1
    print(result)