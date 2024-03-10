import sys

n, m = map(int,sys.stdin.readline().split())

heard_words = set([sys.stdin.readline().rstrip() for _ in range(n)])
watch_words = set([sys.stdin.readline().rstrip() for _ in range(m)])
duplicates = set()

for i in heard_words:

    if i in watch_words:
        duplicates.add(i)

sorted_list =sorted(duplicates)
print(len(sorted_list))
for i in sorted_list:
    print(i)


