import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int,input().split()))

M = int(input())
test = list(map(int,input().split()))

count = {}

for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for target in test:
    result = count.get(target) # target : 2  같은 타겟의 대한 값을 가져옴
    if result == None:
        print(0, end=' ')
    else:
        print(result, end=' ')