num = int(input())

result = []
for i in range(1, num+1):
    if num % i == 0:
        result.append(i)

print("약수:", end=" ")
for i in result:
    print(i, end=" ")

print("\n합:", sum(result))