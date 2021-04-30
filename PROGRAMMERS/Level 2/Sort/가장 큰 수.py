
# 정렬 - 가장 큰 수

def solution(numbers):
  num = list(map(str, numbers))
  num.sort(key=lambda x : x * 3, reverse=True)
  return str(int(''.join(num)))

solution([3, 30, 34, 5, 9])