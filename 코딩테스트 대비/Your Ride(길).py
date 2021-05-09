# Your Ride(길)

from functools import reduce


def multiply(arr):
    return reduce(lambda x, y: x * y, arr)


alphabets = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
             "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19,
             "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26, }

group_name = input()
comet_name = input()

group_name_val = [alphabets.get(i) for i in group_name]
comet_name_val = [alphabets.get(i) for i in comet_name]

group_m, group_n = divmod(multiply(group_name_val), 47)
comet_m, comet_n = divmod(multiply(comet_name_val), 47)

if group_n == comet_n:
    print('GO')
else:
    print('STAY')

# COMETHALEBOPP
# HEAVENSGATE

# SHOEMAKERLEVY
# USACO
