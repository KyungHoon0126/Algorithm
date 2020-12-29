'''
함수
'''


def add(a, b):
    return a + b


print(add(3, 7))


#  return문 없이 함수를 작성할 수도 있다.
def add(a, b):
    print('함수의 결과 : ', a + b)


add(3, 7)

add(b=3, a=7)

#  함수 안에서 함수 ㅂ밖의 변수 데이터를 변경해야할 때 global 키워드 이용.
#  global 키워드로 변수를 지정하면, 해ㅑ당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조.

a = 0


def func():
    global a
    a += 1


for i in range(10):
    func()

print(a)


def add(a, b):
    return a + b


#  일반적인 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print('람다 : ', (lambda a, b: a + b)(3, 7))
