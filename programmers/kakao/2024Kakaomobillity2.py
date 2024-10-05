def cTime(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s


def cSeconds(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02}:{m:02}:{s:02}"


def isflag(currentT):
    currentT = currentT.replace(':', '')
    lst = set(currentT)
    return len(lst) <= 2


def Solution(S, T):
    startSeconds = cTime(S)
    endSeconds = cTime(T)
    count = 0

    for i in range(startSeconds, endSeconds + 1):
        currentT = cSeconds(i)
        if isflag(currentT):
            count += 1
    return count

S = "10:10:00"
T = "10:10:05"
print(Solution(S, T))
