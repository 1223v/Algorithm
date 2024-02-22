n = int(input())
m = int(input())

print(n*(m % 10))
print(n*((m % 100 - m % 10) // 10))
print(n*(m-(m % 100))//100)
print(n * m)