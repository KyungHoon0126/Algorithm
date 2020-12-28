'''
Shift + F10 : 실행, Shift + F9 : 디버그, 한 줄 디버깅 : Shift + F7
디버깅 종료 : Shift + F9
자동 정렬 : Ctrl + Alt + L
'''

'''
수 자료형
'''

d = 1000
print(d)

d = -7
print(d)

d = 157.93  # 양의 실수
print(d)

d = -1837.2  # 음의 실수
print(d)

# 소수부가 0일때 0을 생략
d = 5.
print(d)

# 정수부가 0일때 0을 생략
d = -.7
print(d)

'''
e 다음에 오는 수는 10의 지수부를 의미한다.
'''

# 10억의 지수 표현 방식
d = 1e9  # 1000000000.0
print(d)

d = 75.25e1  # 752.5
print(d)

d = 3954e-3  # 3.954
print(d)

# 2진수에서는 표현한 값이 정확히가 아닌 미세한 오차가 발생. => 컴퓨터가 실수를 정확히 표현하지 못한다.
d = 0.3 + 0.6  # 0.8999999999999999
print(d)

if d == 0.9:
    print(True)
else:
    print(False)

# 소수점 값을 비교하는 작업이 필요한 문제라면 실수 값을 비교하지 못해서 원하는 결과를 얻지 못할 수 있다.
# 이럴 때는 round() 함수를 이용
# 첫 번째 인자 : 실수형 데이터, 두 번째 인자 : 반올림하고자 하는 위치 / 두 번째 인자없이 인자를 하나만 넣을때는 소수점 첫째 자리에서 반올림한다.

d = 0.3 + 0.6
print(round(d, 4))  # 0.9

if round(d, 4) == 0.9:
    print(True)
else:
    print(False)

d = 1234.567
print(round(d, 1))  # 1234.6

# 수 자료형의 연산
# 파이썬에서 나누기 연산자(/)는 나눠진 결과를 기본적으로 실수형으로 처리.
# 나머지 연산자 : %, 나눈 결과에서 몫만을 얻고자 할 때 몫 연산자 (//)를 이용

a = 7
b = 3

# 나누기
print(a / b)  # 2.3333333333333335

# 나머지
print(a % b)

# 몫
print(a // b)

# 거듭제곱 연산자(**)
a = 5
b = 3
print(a ** b)

'''
리스트 자료형
'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# 인덱스 4, 즉 다섯 번째 원소에 접근
print(a[4])

# 빈 리스트 선언 방법 1)
a = list()
print(a)

# 빈 리스트 선언 방법 2)
a = []
print(a)

# 크기가 N인 1차원 리스트 초기화
# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

# 인덱스값을 입력하여 리스트의 특정 원소에 접근하는 것  : 인덱싱, 인덱스값은 양의 정수와 음의 정수 모두 가능, 음의 정수를 넣으면 원소를 거꾸로 탐색
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 뒤에서 첫 번째 원소 출력
print(a[-1])

# 뒤에서 세 번째 원소 출력
print(a[-3])

# 네 번째 원소 값 변경
a[3] = 7
print(a)

# 리스트에서 연속적인 위치를 갖는 원소들을 가져와야 할 때 : 슬라이싱, 대괄호 안에 콜론(:)을 넣어서 시작 인덱스와 긑 인덱스 설정.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 두 번째 원소부터 네 번째 원소까지
print(a[1:4])

# 리스트 컴프리헨션 : 리스트 초기화 방법 중 하나, 대괄호([])안에 조건문과 반복문을 넣는 방식으로 초기화 가능,.

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 위 소스코드를 일반적인 소스코드로 작성 하면 아래와 같다.
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)
print(array)

# 1부터 9까지의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]
print(array)

# N X M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

# 언더바(_) : 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바 사용
for _ in range(5):
    print("Hello World")

# 특정 크기의 2차원 리스트를 초기화할 때는 반드시 리스트 컴프리헨션을 이용해야 한다.
# N x M 크기의 2차원 리스트 초기화(잘못된 방법)
n = 3
m = 4
array = [[0] * m] * n
print(array)

array[1][1] = 5
print(array)
# array[1][1]의 값을 5로 바꾸었을 뿐인데, 3개의 리스트에서 인덱스 1에 해당하는 모든 원소들의 값이 모두 5로 바뀜.
# -> 내부적으로 포함된 3개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식되기 때문. 따라서 반드시 리스트 컴프리헨션을 이용해야함.

# 리스트 관련 기타 메서드 : append(), sort(), reverse(), insert(), count(), remove()
a = [1, 4, 3]
print("기본 리스트 : ", a)

# 리스트에 원소 삽입
a.append(2)
print("삽입: ", a)

# 오름차순 정렬
a.sort()
print("오름차순 정렬: ", a)

# 내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬: ", a)

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: ", a)

# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에 3 추가: ", a)

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))

# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a)

# 특정한 값의 원소를 모두 제거하려면
# 1) a에 포함된 원소를 하나씩 확인하며 그 원소가 remove_set에 포함되어 있지 않았을 때만 리스트 변수인 result에 넣겠다는 의미
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)

'''
문자열 자료형
'''

data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

a = "Hello"
b = "World"

print(a + " " + b)

a = "String"
print(a * 3)

a = "ABCDEF"
print(a[2:4])

# 튜플 : 한 번 선언된 값을 변경할 수 없다.s
a = (1, 2, 3, 4)
print(a)

# a[2] = 7 => 컴파일 에러

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

# 키와 값을 별도로 뽑아내기 위한 함수들이 있다.
# 키 데이터만 뽑아서 리스트로 이용할 때 : keys() / 값 데이터만을 뽑아서 리스트로 이용할 때 : values()

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()

# 값 데이터만 담은 리스트
value_list = data.values()

print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

# 집합 자료형 : 🔶 중복을 허용하지 않음, 순서가 없음. 🔶
# 특정한 데이터가 이미 등장한 적이 있는지 여부를 체크할 때 매우 효과적.
# 집합자료형 초기화할 때 : set() 이용하거나 중괄호({})안에 각 원소를 콤마(,)를 기준으로 구분해서 넣으면 된다.
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

data = {1, 1, 2, 3, 4, 4, 5}
print(data)

# 집합 자료형의 연산
# 합집합 계산 : '|' / 교집합 : '&' / 차집합 : '-'

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print('합집합 : ', a | b)  # 합집합
print('교집합 : ', a & b)  # 교집합
print('차집합 : ', a - b)  # 차집합
print(b - a)

# 집합 데이터에 값을 추가할 때 : add(), 여러 개의 값을 한꺼번에 추가하고자 할 때 : update(), 특정한 값을 제거할 때 : remove()
data = set([1, 2, 3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5, 6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)
