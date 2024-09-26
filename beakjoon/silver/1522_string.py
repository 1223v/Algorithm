

s = input()
a = s.count('a')
k = s + s


min_value = float('inf')

for i in range(len(k) -len(s)):
    min_value = min(min_value, k[i:i+a].count('b'))
print(min_value)