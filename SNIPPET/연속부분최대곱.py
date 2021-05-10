# 방법 1
from functools import reduce


def multiply(arr):
    return reduce(lambda x, y: x * y, arr)


cnt = int(input())
data = []
result = []

for i in range(cnt):
    data.append(float(input()))

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if len(data[i:j]) == 1:
            result.append(data[i:j][0])
        else:
            result.append(round(multiply(data[i:j]), 3))

print(max(result))


# 방법 2
cnt = int(input())
now = 0.0
dMax = 0.0

for i in range(0, cnt):
    temp = float(input())

    if now >= 1.0:
        now *= temp
    else:
        now = temp
    if now > dMax:
        dMax = now

print('%.3f' % dMax)
