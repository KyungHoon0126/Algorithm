# Calculator.py
# 단축키
# CTRL + / : 주석문 설정/해제
# Tab : 들여쓰기
# Shift + Tab : 들여쓰기 해제

# Ctrl + Shift + F10 : 최초 작성 코드의 실행, 마우스 오른쪽버튼으로 메뉴선택하여 실행.
# Shift + F10 : 마지막에 실행했던 코드를 다시 실행, 실행 아이콘을 클릭

def add(a,b):
    c = a + b
    print('add called')
    return c

def subtract(a,b):
    c = a - b
    return c

def multiply(a,b):
    c = a * b
    return c

def divide(a,b):
    c = a / b
    return c

# main, 여러 코드들을 구분할 때 하나의 모듈이라고 부른다, 최상위 모듈
if __name__ == '__main__':
    print(add(10, 20))
    print(subtract(30, 10))
    print(multiply(3, 5))
    print(divide(30, 3))


# main 처리를 해주지 않으면, 이 모듈을 사용하는 다른 py 파일에서 다른 py 파일의 내용만 출력되는것이 아니라 이 모듈을
# 정의한 곳의 내용도 출력된다.