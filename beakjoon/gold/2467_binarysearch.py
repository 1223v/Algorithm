import sys
input = sys.stdin.readline

N = int(input())
s = list(map(int,input().split()))


start = 0
end = len(s)-1
#https://www.acmicpc.net/problem/2467

        if first_tmp == 0:
            break

    if tmp < 0:
        start += 1

    else:
        end -= 1

print(s[left_idx],s[right_idx])
