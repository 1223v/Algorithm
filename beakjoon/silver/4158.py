import sys
input = sys.stdin.readline

while True:
    N,M = map(int,input().split())

    if N==0 and M == 0:
        exit(0)

    m_lst = [int(input()) for _ in range(N)]
    g_lst = [int(input()) for _ in range(M)]

    m_chk, g_chk = 0,0
    result = 0

    while m_chk < N and g_chk < M:
        if m_lst[m_chk] == g_lst[g_chk]:
            result += 1
            m_chk += 1
            g_chk += 1

        elif m_lst[m_chk] < g_lst[g_chk]:
            m_chk+=1

        else:
            g_chk+=1

    print(result)



