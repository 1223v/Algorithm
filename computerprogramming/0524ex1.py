def func(numbers, index=-1):

    number = numbers[index]
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    return count


print(func([3, 5, 8, 24, 12], 3))
print(func([3, 5, 8, 24, 12]))
