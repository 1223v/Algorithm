import sys
input = sys.stdin.readline

N = int(input())
magic = 0
cat = 0

while N > cat:
    if cat == 0:
        cat += 1
    else:
        cat *= 2

    magic += 1

print(magic)
