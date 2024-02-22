n, m = map(int, input().split())

# 돈 단위 입력 받기
money_menu = [(int(input())) for _ in range(n)]
money_menu.sort(reverse=True)
cnt = 0
for i in money_menu:
    if m // i > 0:

        cnt += m // i
        m = m % i

    elif m < 0:
        break


print(cnt)