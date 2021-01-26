# 5 9 3
# 2 4 5 4 6
# 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 + 6 = 46
# 반복되는 수열 : 6 + 6 + 6 + 5
# 반복되는 수열의 길이 : k + 1
# 반복되는 수열의 횟수 : int(m / (k + 1))
# 제일 큰 수 반복 횟수 : (m / (k + 1)) * k
# 나누어 떨어지지 않는 경우 : int(m % (k + 1))

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n - 1]
second = data[n - 2]

result = 0
count = 0   # 제일 큰 수 반복 횟수

count += int(m / (k + 1) * k)
count += int(m % (k + 1))

result += count * first
result += (m - count) * second

print(f"합 : {result}")
