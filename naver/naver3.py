def sol2(A,S):
    result = 0
    AL = [0] * int(len(A)+1)
    AL[0] = 0
    AL[1] = A[0]
    for i in range(2, len(A)+1):
        AL[i] = AL[i - 1] + A[i-1]

    for i in range(0,len(AL)):
        for j in range(1,len(AL)):
            Alength = j - i if j - i > 0 else 1
            Aresult = (AL[j]-AL[i]) / Alength

            if float(S) == Aresult:
                result += 1
    return 1000000000 if result > 1000000000 else result

