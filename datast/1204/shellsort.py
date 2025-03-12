def shell_sort(a):
    n = len(a)
    h = n // 2  # 초기 gap 크기 설정

    print("초기 배열:", a)

    while h > 0:
        print(f"\ngap 크기: {h}")
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        print(f"배열 상태: {a}")
        h //= 2  # gap 크기 절반으로 줄임

    return a


# 예시 데이터
data = [5, 3, 8, 4, 2, 7, 1, 6]

# 셸 정렬 실행
sorted_data = shell_sort(data)
print("\n최종 정렬된 배열:", sorted_data)
