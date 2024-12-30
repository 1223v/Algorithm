import sys
input = sys.stdin.readline

N = list(map(int,input().rstrip()))

num_lst = [1,2,3,4,5,7,8,0]
max_value = 0
count = 0
for i in num_lst:
    tmp = N.count(i)
    max_value = max(max_value, tmp)

six_nine_count = N.count(6) + N.count(9)
tmp2 = six_nine_count // 2 + six_nine_count % 2

if tmp2 > max_value:
    print(tmp2)

else:
    print(max_value)




