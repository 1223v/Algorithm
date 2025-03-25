import sys
input = sys.stdin.readline

N,M = map(int,input().split())
s = list(map(int,input().split()))

# 윤호는 오차 없이 일급을 따박따박 당일에 받음
# 각 날마다 일차이

length = len(s)
prefix_sum = [0] * ((length * 2)+1)
for i in range(length):
    prefix_sum[i+1] = prefix_sum[i] + s[i%N]

count = 0

for i in range(length):
    count = max(count,prefix_sum[i+M] - prefix_sum[i])


print(count)

