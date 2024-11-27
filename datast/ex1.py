def insert(bag, e):
    bag.append(e)

import time
myBag= []
start = time.time()

for _ in range(10000000):
    insert(myBag, '축구공')

end = time.time()
print("실행시간 = ",end-start)