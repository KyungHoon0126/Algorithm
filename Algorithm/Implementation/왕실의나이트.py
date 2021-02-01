'''
ord
ord(c)는 문자의 아스키 코드 값을 돌려주는 함수이다.

※ ord 함수는 chr 함수와 반대이다.

>>> ord('a')
97
>>> ord('0')
48
'''

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0

# input_data[0] = a, input_data[1] = 1
# a - 'a'의 아스키 코드 값을 뺀거에 1을 더한 값 => 즉 ord('a')는 97이므로 97 - 97 + 1 = 1이 된다.
print(ord('a'))
print(row)  # 1
print(column)  # 1
