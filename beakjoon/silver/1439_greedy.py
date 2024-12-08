# 신박
import sys
input = sys.stdin.readline

s = input().rstrip()

a1 = s.split('0')
a2 = s.split('1')

zero = len(a1) - a1.count('')
one = len(a2) - a2.count('')

min_value = min(zero, one)
print(min_value)