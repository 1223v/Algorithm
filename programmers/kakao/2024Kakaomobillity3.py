def solution(D, T):
    t = [[0] * 3 for _ in range(len(D))]  # D의 길이에 맞는 2차원 리스트 생성
    for i in range(len(T)):
        for j in range(len(T[i])):
            if T[i][j] == 'P':
                t[i][0] += 1
            elif T[i][j] == 'G':
                t[i][1] += 1
            elif T[i][j] == 'M':
                t[i][2] += 1

    car = [0] * 3
    for i in range(3):
        tmp = 0
        for j in range(len(D)):
            tmp += D[j]
            if t[j][i] == 0:
                continue
            else:
                car[i] += t[j][i]
                car[i] += tmp * 2
                tmp = 0

    print(max(car))

# Example usage
D = [2, 5]
T = ["PGP", "M"]
solution(D, T)
