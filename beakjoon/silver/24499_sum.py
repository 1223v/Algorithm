import sys
input = sys.stdin.readline

N,K = map(int,input().split())
k_lst = [0] + list(map(int,input().split()))
k_lst += k_lst[1:-1]
S = [0] * (N*2)
S[0] = 0
S[1] = k_lst[1]


for i in range(1,(N*2)):
    S[i] = S[i-1] + k_lst[i]


max_value = 0

for i in range(N*2-K):
    max_value = max(max_value, S[i+K] - S[i])

print(max_value)

