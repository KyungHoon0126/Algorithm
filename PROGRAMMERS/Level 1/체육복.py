def solution(n, lost, reserve):
  # 체육복을 도난당한 학생 번호
  lost_numbers = [i for i in lost if i not in reserve] # 여유분이 없고 도난당한 학생만 필터.

  # 체육복을 빌려줄 수 있는 학생 번호
  lendable_numbers = [i for i in reserve if i not in lost] # 여유분을 가지고 있지만 자신이 도난당했을 수도 있기 때문에 if 조건으로 필터.

  for i in lendable_numbers:
    # i를 기준으로 왼쪽 번호 먼저 확인 후 오른쪽 번호를 확인한다.
    left = i - 1 # 0, 2 왼쪽번호
    right = i + 1 # 2, 4 오른쪽번호

    if left in lost_numbers:
      lost_numbers.remove(left)
    elif right in lost_numbers:
      lost_numbers.remove(right)

  return n - len(lost_numbers)

solution(5, [2, 4], [1, 3, 5])