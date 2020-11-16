
current = 75E3
limit = 25E3

for i in range(1, 36):
    current += 25E3
    current *= 1.07
    limit *= 1.02
    print("{0}: {1}".format(2020+i, current))
