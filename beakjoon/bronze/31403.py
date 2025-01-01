import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()
C = input().rstrip()

result1 = int(A) + int(B) - int(C)
result2 = int(A+B) - int(C)

print(result1)
print(result2)
