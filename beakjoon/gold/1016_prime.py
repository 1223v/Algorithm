import sys
import math
input = sys.stdin.readline

Min, Max = map(int,input().split())
check = [False] * (Max - Min +1)

for i in range(2, int(math.sqrt(Max)+1)):
    pow = i * i
    start_index = int(Min/pow) # 최솟값 / 제곱수 => Min과 Max 사이에서 제곱수의 배수가 어디서부터 시작하는지를 찾음
    # 예) Min = 10, pow = 4 => 10 / 4 = 2 ... 2 아래 조건문에 의해 start_index = 3 -> 아래에서 항상 +1 하므로 4부터 시작임을 알수 있음
    if Min % pow != 0:
        start_index += 1

    for j in range(start_index, int(Max/pow)+1): # 제곱수를 True로 변경
        check[int((j*pow) - Min)] = True

count = 0

for i in range(0, Max-Min+1):
    if not check[i]:
        count += 1

print(count)
