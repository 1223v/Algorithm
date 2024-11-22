import sys
input = sys.stdin.readline

N = int(input())

# 1개 혹은 3개
chk = -1
while N >0:
    chk = -chk
    if N - 3 >0:
        N -= 3
    else:
        N -= 1



if chk == 1:
    print("SK")
else:
    print("CY")