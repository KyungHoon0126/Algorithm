n, k = map(int, input().split())
result = 0

# 1
# # N이 K 이상이라면 K로 계속 나누기
# while n >= k:
#     # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
#     while n % k != 0:
#         n -= 1
#         result += 1
#     # K로 나누기
#     n //= k
#     result += 1
#
# # 마지막으로 남은 수에 대하여 1씩 빼기
# while n > 1:
#     n -= 1
#     result += 1
#
# print(result)

# 25 5

# 2
n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될때까지 1씩 빼기
    target = (n // k) * k  # N을 K로 나눈 몫에 K를 곱해주면 나눌 수 있는 제일 큰 수가 나온다.
    result += (n - target)  # result에 1을 몇 번 빼야하는지 더한다.
    n = target  # n을 나눌 수 있는 제일 큰 수를 구했고 1을 몇번 빼야하는지 더했으므로, n을 target으로 바꿔준다.
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1  # 현재 n이 나누어 떨어지는 수이므로 result에 1을 더해주고
    n // k  # k로 나누어준다.

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
