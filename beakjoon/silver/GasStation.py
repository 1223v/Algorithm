import sys

n = int(sys.stdin.readline())

city = list(map(int,input().split()))
stations_price = list(map(int, input().split()))
sum = 0
cheap = stations_price[0]
for i in range(0,n-1):

    if cheap > stations_price[i]:
        cheap = stations_price[i]
    sum += cheap*city[i]

print(sum)