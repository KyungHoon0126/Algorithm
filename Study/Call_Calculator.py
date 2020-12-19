# Call_Calculator.py

# import Calculator

# Calculator에 add가 내장되 있더라도, 어디에 있는지 알려주어야 사용이 가능하다.
# print(add(10, 20)) → 즉 이 상태에서는 오류가 발생한다.

# 올바른 사용 방법
# print(Calculator.add(20, 30))


# ----------------------------------------------------------------------------------------------------------------------


# Calculator. ~ : Calculator에 있는 것들을 사용하기 위해서는 Calculator. ~ 을 다 써줘야 한다.
# 이런 불편함을 감소하기 위해서 as 를 이용해 이름을 줄일 수 있다.

import Calculator as Cal

print(Cal.add(20, 30))
print(Cal.subtract(50, 10))
print(Cal.multiply(2, 5))
print(Cal.divide(40, 2))


# ----------------------------------------------------------------------------------------------------------------------

# 패키지 설치 방법

# Terminal → pip install 사용할 패키지 이름
# file → settings → Project: 프로젝트명 → Project interpreter → +