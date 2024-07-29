import sys
input = sys.stdin.readline

n = int(input())

def gcd(a,b):

    if b ==0:
        return a
    else:
        return gcd(b, a%b)



for _ in range(n):
    n,m = map(int, input().split())
    x = (n*m)/gcd(n,m)
    print(int(x))