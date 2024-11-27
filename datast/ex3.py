def hanoi(n, s, t, a):
    if n == 1:
        print(f"{s} --> {t}")
        return

    hanoi(n - 1, s, a, t)
    print(f"{s} --> {t}")
    hanoi(n - 1, a, t, s)

# n=3일 때 실행
n = 3
hanoi(n, 'A', 'C', 'B')
