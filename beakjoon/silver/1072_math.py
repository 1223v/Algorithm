# # https://www.acmicpc.net/problem/1072
# import sys
# import math
# input = sys.stdin.readline
#
# X, Y = map(int,input().split())
# check = (Y * 100) // X
#
# if check>=99:
#   print(-1)
#
# else:
#     check += 1
#     k = ((check*X)-(100*Y)) / (100-check)
#     result = math.ceil(k)
#
#     print(result)

# https://www.acmicpc.net/problem/1072
import sys
import math
input = sys.stdin.readline

X, Y = map(int,input().split())
check = int((Y*100)/X)

if check>=99:
  print(-1)

else:
    check+=1
    k = ((check*X)-(100*Y)) / (100-check)

    result = math.ceil(k)

    print(result)
