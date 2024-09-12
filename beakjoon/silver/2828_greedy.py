import sys
input = sys.stdin.readline

n,m = map(int,input().split())
count = int(input())
start = 1
end = start + m
result = 0
for i in range(count):
    apple = int(input()) #1
    if start <= apple < end:
        pass
    elif apple < start: # 떨어지는 사과가 바구니보다 왼쪽인 경우
        result += start - apple
        start = apple
        end = start + m
    else: # 떨어지는 사과가 바구니의 오른쪽인 경우
        result += apple+1 - end
        end = apple+1
        start = end - m

print(result)