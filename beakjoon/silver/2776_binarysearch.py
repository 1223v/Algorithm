import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N1 = int(input())
    note1 = list(map(int,input().split()))

    N2 = int(input())
    note2 = list(map(int,input().split()))

    note1.sort()

    for i in note2:

        start = 0
        end = len(note1)-1
        check = 0
        while start <= end:
            mid = int((start+end) / 2)
            if i == note1[mid]:
                check = 1
                break

            elif note1[mid] < i:
                start = mid + 1

            else:
                end = mid - 1

        print(check)


