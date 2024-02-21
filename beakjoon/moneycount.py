# import sys
# money = int(sys.stdin.readline()) # 거슬러줘야 되는 거스름돈 액수

# cnt = 0
# while money > 0:
#
#     if money % 5 ==0:
#
#         cnt += money // 5
#         break
#     else:
#         money -= 2
#         cnt += 1
#
# if money < 0:
#     print(-1)
# else:
#     print(cnt)


import sys
money = int(sys.stdin.readline()) # 거슬러줘야 되는 거스름돈 액수
if money in [1, 3]:
    print(-1)
    exit(0)

# 5원짜리 동전의 개수 N
# 2원짜리 동전의 개수 M

# 거스름돈을 줄 수 있는 경우
# 1) 5원짜리를 최대한 많이 준다.
N = money // 5
M = (money - N * 5) // 2
if (money - N * 5) % 2 == 0:
    print(N + M)
    exit(0)


# 2) 5원 짜리를 최대한 많이 주는 것 보다 1개 적게 주고 나머지를 2원짜리로 준다.
N = money // 5 - 1
if N > 0:
    money -= N * 5
M = money // 2
print(N+M)

