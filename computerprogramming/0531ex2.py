import random

def lotto_numbers():
    lottonumbers = set()

    while len(lottonumbers) < 8:
        lottonumbers.add(random.randint(1, 60))

    return lottonumbers


lottonumbers = lotto_numbers()
print(lottonumbers)
