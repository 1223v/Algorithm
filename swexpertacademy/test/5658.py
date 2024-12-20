TC = int(input())

for t in range(TC):
    N, K = map(int,input().split())
    lst = input()
    cnt = N // 4
    result = []

    for i in range(cnt):
        lst = lst[-1] + lst[:-1]
        for j in range(0,N,cnt):
            result.append(lst[j:j+cnt])

    set_result = set([int(num,16) for num in result])
    sorted_result = sorted(list(set_result),reverse=True)

    print(f"#{t+1} {sorted_result[K-1]}")