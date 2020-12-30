n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k
count += m % (k + 1)  # 나누어 떨어지지 않는 경우

result = 0
result += count * first
result += (m - count) * second

print(result)
