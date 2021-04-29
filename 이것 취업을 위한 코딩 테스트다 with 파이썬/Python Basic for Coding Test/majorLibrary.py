'''
주요 라이브러리의 문법

https://rfriend.tistory.com/327
'''

'''
내장 함수
'''

result = sum([1, 2, 3, 4, 5])
print(result)

#  min() : 파라미터가 2개 이상 들어왔을 때 가장 작은 값 반환
result = min(7, 3, 5, 2)
print(result)

result = max(7, 3, 5, 2)
print(result)

#  eval() : 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환
result = eval("(3 + 5) * 7")
print(result)

result = sorted([9, 1, 8, 5, 4])  # 오름차순으로 정렬
print(result)

result = sorted([9, 1, 8, 5, 4], reverse=True)  # 내림차순으로 정렬
print(result)

result = sorted([('홍길동', 35), ('이순신', 75), ('이무개', 50)], key=lambda x: x[1], reverse=True)
print(result)

'''
itertools - 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리
'''

from itertools import permutations

#  데이터 준비
data = ['A', 'B', 'C']

#  permutations : 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든경우(순열)를 계산해준다.

#  모든 순열 구하기
result = list(permutations(data, 3))

print("permutations : ", result)

#  combinations : 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)을 계산한다.

from itertools import combinations

data = ['A', 'B', 'C']

#  2개를 뽑는 모든 조합 구하기
result = list(combinations(data, 2))
print("combinations : ", result)

#  product : permutations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산. 다만 원소를 중복하여 뽑는다.
#  객체를 초기화 할 때는 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어준다.

from itertools import product

data = ['A', 'B', 'C']
#  2개를 뽑는 모든 순열 구하기(중복 허용)
result = list(product(data, repeat=2))
print("product : ", result)

#  combinations_with_replacement : combinations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)을 계산한다. 다만 원소를 중복해서 뽑는다.

from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
#  2개를 뽑는 모든 조합 구하기(중복 허용)
result = list(combinations_with_replacement(data, 2))
print("combinations_with_replacement : ", result)

'''
heapq - 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용
'''

import heapq


def heaposort1(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heaposort1([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print("heapsort : ", result)


#  최대 힙

def heapsort2(iterable):
    h = []
    result = []

    #  모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    #  힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


result = heapsort2([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print("max heap : ", result)

'''
bisect : 이진 탐색
'''

#  bisect_left : 정렬된 순서를 유지하면서 가장 왼쪽 인덱스를 찾는 메서드
#  bisect_right : 정렬된 순서를 유지하도록 가장 오른쪽 인덱스를 찾는 메서드

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print("bisect_left : ", bisect_left(a, x))
print("bisect_right : ", bisect_right(a, x))


#  bisect_left()와 bisect_right() 함수는 '정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구할때 효과적이다.
#  count_by_range(a, left_value, right_value) : 정렬된 리스트에서 값이 [left_value, right_value]에 속하는 데이터의 개수를 반환한다.

#  값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


#  리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

#  값이 4인 데이터 개수 출력
print("count_by_range : ", count_by_range(a, 4, 4))

#  값이 [-1, 3] 범위에 있는 데이터 개수 출력
print("count_by_range : ", count_by_range(a, -1, 3))

'''
collections - deque, Counter
'''

from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)  # 첫 번째 인덱스에 삽입
data.append(5)

print("deque : ", data)
print("deque to list : ", list(data))  # 리스트 자료형으로 변환

# Counter : 등장 횟수를 세는 기능 제공, iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려준다.
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter)
print("counter : ", counter['blue'])  # 'blue'가 등장한 횟수 출력
print("counter : ", counter['green'])  # 'green'이 등장한 횟수 출력
print("counter to dict : ", dict(counter))  # 사전 자료형으로 변환


'''
math
'''

import math
print("factorial 5! : ", math.factorial(5))

#  sqrt() : 제곱근 반환
print("sqrt : ", math.sqrt(7))

#  gcd() : 최대 공약수를 구해줌.
print("gcd : ", math.gcd(21, 14))

print("pi : ", math.pi, "e : ", math.e)
