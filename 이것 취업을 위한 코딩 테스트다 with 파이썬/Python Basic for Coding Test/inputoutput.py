'''
입출력
'''

#  데이터의 개수 입력
n = int(input())

#  각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

#  n, m, k를 공백으로 구분하여 입력
n, m, k = map(int, input().split())

print(n, m, k)

#  파이썬의 경우 입력의 개수가 많은 경우에는 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 함수를 이용
#  import sys

#  sys.stdin.readline().rstrip()

#  sys 라이브러리를 사용할 때는 한 줄 입력을 받고 나서 rstrip() 함수를 꼭 호출해야 한다.
#  readline()으로 입력하면 입력 후 엔터가 줄 밖 기호로 입력되는데, 이 공백 문자를 제거하려면 rstrip() 함수를 사용해야 한다.

import sys

# 문자열 입력받기
data = sys.stdin.readline().rstrip()
print(data)

answer = 7
print("정답은 " + str(answer) + "입니다.")

print("정답은 ", str(answer), "입니다.")

#  f-string : 문자열 앞에 접두사 'f'를 붙임으로써 사용 가능, 단순히 중괄호({}) 안에 변수를 넣음을써, 자료형의 변환 없이도 문자열과 정수를 함께 넣을 수 있다.
print(f"정답은 {answer}입니다.")
