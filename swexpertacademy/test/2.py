def cal(n,A,B):
    max_value = 0
    for i in range(n):
        for j in range(n):
            k = 0
            count = 0
            while i+k < n and j+k < n:
                if A[i+k] == B[j+k]:
                    count += 1
                else:
                    break
                k+= 1
            max_value = max(max_value, count)
    return max_value

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int, input().split()))
    cnt = cal(N,A,B)
    print("#%d %d" % (test_case, cnt))