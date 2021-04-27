# 윤년 판별

# 평년 : 연도가 4로 나누어 떨어지지 않음.
# 윤년 : 연도가 4로 나누어 떨어지지만 100으로 나누어 떨어지지 않음.
# 평년 : 연도가 4와 100으로 나누어 떨어지지만 400으로 나누어 떨어지지 않음.
# 윤년 : 연도가 4, 100, 400으로 나누어 떨어진다.

# calendar 모듈을 이용해 isleap() 메서드를 이용하면 윤년 판별을 할 수 있다.
import calendar
calendar.isleap()

# 기간을 설정해 윤년이 몇 번 있는지 반환해 주는 함수.
# 단, 종료 연도는 포함되지 않는다.
y1 = 1804
y2 = 2096
calendar.leapdays(y1, y2)


# 윤년 판별 함수.
def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True