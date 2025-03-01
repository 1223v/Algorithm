import sys
input = sys.stdin.readline

N,K = map(int,input().split())
k_lst = [0]+list(map(int,input().split()))
S = [0] * (N+1)
S[1] = k_lst[1]

for i in range(1,N):
    S[i] = S[i-1] + k_lst[i]

max_value = 0

for i in range(1,(N+1)*2):
    max_value = max(max_value, S[(i+K+1)//K] + S[(i+K+1)%K]-S[(i-1)%K])

print(max_value)
