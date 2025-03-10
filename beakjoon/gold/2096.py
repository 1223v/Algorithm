import sys
input = sys.stdin.readline

N = int(input())

a,b,c= map(int,input().split())
a1,b1,c1 = a,b,c

for _ in range(1,N):

    x,y,z= map(int,input().split())
    k1 = max(x + a, x + b)
    k2 = max(y + a, y + b, y + c)
    k3 = max(z + b, z + c)

    k4 = min(x + a1, x + b1)
    k5 = min(y + a1, y + b1, y + c1)
    k6 = min(z + b1, z + c1)

    a,b,c = k1,k2,k3
    a1,b1,c1 = k4,k5,k6

print(max(a,b,c), min(a1,b1,c1))






