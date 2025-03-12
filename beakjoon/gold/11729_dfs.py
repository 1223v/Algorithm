# 1. 시작 -> 임시
# 2. 큰 원반 끝으로 이동
# 3. 임시 -> 시작

import sys
input = sys.stdin.readline

N = int(input())
result = 0
result_value = []
def hanoi(n,from_value, tmp_value, to_value):
    global result
    if n == 1:
        result_value.append((from_value, to_value))
        # print(from_value, to_value) # 큰원반
        # print(5555555)
        result += 1
        return

    hanoi(n-1,from_value, to_value, tmp_value) # from -> tmp 임시 to
    result_value.append((from_value, to_value))
    # print(from_value, to_value)
    result += 1
    hanoi(n-1,tmp_value, from_value, to_value) # tmp -> to 임시 from

hanoi(N,1,2,3)
print(result)
for i in result_value:
    print(*i)