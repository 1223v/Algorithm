import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    input()
    N,M = map(int,input().split())

    S1 = list(map(int,input().split()))
    B1 = list(map(int,input().split()))
    S1.sort()
    B1.sort()

    while len(S1) > 0 and len(B1) > 0:

        if S1[0] < B1[0]:
            S1.pop(0)
        elif S1[0] > B1[0]:
            B1.pop(0)
        else:
            B1.pop(0)

    if len(S1):
        print("S")
    elif len(B1):
        print("B")
    else:
        print("C")