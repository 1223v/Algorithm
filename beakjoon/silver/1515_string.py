import sys
input = sys.stdin.readline

s = input().rstrip()
result = 1
idx=0
while True:
    for i in str(result):
        if i == s[idx]:
            idx += 1
            if idx == len(s):
                print(result)
                exit()

    result += 1




