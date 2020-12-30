n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n - 1]  # Max
second = data[n - 2]  # Min

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
