'''
조건문
'''
x = 15
if x >= 10:
    print(x)

score = 70
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('F')

# 아무것도 처리하고 싶지 않을 때 : pass
score = 85

if score >= 80:
    pass  # 나중에 작성할 소스코드
else:
    print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다.')

if score >= 80:
    result = "Success"
else:
    result = "Fail"

# 조건부 표현식
result = "Success" if score >= 80 else "Fail"
print(result)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = []
result = [i for i in a if i not in remove_set]
print(result)

# 조건문 내에서 부등식
x = 15
if x > 0 and x < 20:
    print("x는 0 이상 20 미만의 수입니다.")

if 0 < x < 20:
    print("x는 0 이상 20 미만의 수입니다.")
