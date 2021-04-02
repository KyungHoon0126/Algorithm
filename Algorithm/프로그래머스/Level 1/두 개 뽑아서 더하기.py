from itertools import combinations

def solution(numbers):
    answer = []
    print(f'가능한 경우의 수 : {list(combinations(numbers, 2))}')
    for i in list(combinations(numbers, 2)):
      answer.append(sum(i))
    return sorted(list(set(answer)), reverse=False)

solution([2,1,3,4,1])