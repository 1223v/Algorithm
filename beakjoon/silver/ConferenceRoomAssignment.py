import sys

n = int(sys.stdin.readline())
room_time = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

room_time.sort(key=lambda x : (x[1],x[0]))
cnt = 1
end_time = room_time[0][1]

for i in range(1, n):
    if room_time[i][0] >= end_time:
        cnt += 1
        end_time = room_time[i][1]


print(cnt)



