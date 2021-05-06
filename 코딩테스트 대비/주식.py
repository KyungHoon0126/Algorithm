# 3번 - 주식

'''
주식 시장 마감 : 마지막에 받는 시간을 기준으로 잡는다.
현재 시간에서 다음 시간 사이까지는 그 가격으로 유지된다 라고 생각한다.

주식시장 마감 40분 이후 부터는 ±5% 값 미만 및 초과가 1분이상 유지되어도 No value.

±5% 값 미만 및 초과인 값이 한시간에서 다음시간 사이의 간격에 포함되어 있고 1분 이상 유지되면 ★
'''

import datetime

# TEST CASE 1
# array = ["13:20:00 200", "13:22:00 250", "13:22:30 202", "15:50:00 100", "16:50:00 205"]
# n = 200  # 기준 값
# OUTPUT : "15:51:00"

# TEST CASE 2
# array = ["13:20:00 200", "13:22:00 250", "13:22:30 202", "15:50:00 100", "16:00:00 205"]
# n = 200
# OUTPUT : "no value"

# TEST CASE 3
array = ["13:20:00 200", "13:22:00 250", "13:23:30 202", "15:50:00 100", "16:00:00 205"]
n = 200
# OUTPUT : "13:23:00"

# 주식 변동 시간 배열
stock_times = []
# 주식 변동 값 배열
stock_values = []

for i in array:
    stock_time, stock_value = i.split(' ')
    stock_times.append(stock_time)
    stock_values.append(stock_value)

print(f"stock_times : {stock_times}")
print(f"stock_values : {stock_times}")

# 주식 시장 마감 40분 전 비교를 위한 마지막 변동 가능 시간
stock_close_hour, stock_close_minute, stock_close_second = map(int, stock_times[-1].split(':'))
if stock_close_minute >= 40:
    stock_close_minute -= 40
else:
    stock_close_hour -= 1
    stock_close_minute = (stock_close_minute + 60) - 40

stock_close_time = datetime.time(stock_close_hour, stock_close_minute, stock_close_second)

print('stock_close_time', stock_close_time)

# +5% 증가 값 : stock_value + 5% 값
# -5% 감소 값 : stock_value - 5% 값
five_percent_value = int(n * (5 / 100))  # 5% 값

flag = False  # 주식이 ★이 되는 구간이 있는지 체크

for i in range(len(array) - 1):
    is_remain_one_minute = False  # ±5% 주식 값이 1분 동안 유지 되는지 체크

    # 현재 시간, 분, 초를 구함.
    current_stock_hour, current_stock_minute, current_stock_second = map(int, stock_times[i].split(':'))
    # 시간 비교를 위해 datetime.time 객체로 변환.
    current_stock_time = datetime.time(current_stock_hour, current_stock_minute, current_stock_second)

    # 유지 시간은 다음 시간에서 현재 시간을 뺀 값이기 때문에 다음 시간을 구함.
    next_stock_hour, next_stock_minute, next_stock_second = map(int, stock_times[i + 1].split(':'))
    # 유지 시간 (다음 시간의 초의 총합에서 현재 시간의 초의 총합을 뺀 것)
    stock_remain_time = ((next_stock_hour * 60 * 60) + (next_stock_minute * 60) + next_stock_second) - (
            (current_stock_hour * 60 * 60) + (current_stock_minute * 60) + current_stock_second)

    print(f'유지 시간 : {stock_remain_time}초')

    if stock_remain_time >= 60:
        is_remain_one_minute = True  # ±5% 주식 값이 1분이상 유지됨.

    print(f'1분 지속 여부 : {is_remain_one_minute}')

    # 현재 시간이 주식 시장 마감 40분에 포함되지 않고
    if current_stock_time < stock_close_time:
        print(f"현재 주식 값 : {int(stock_values[i])}")
        print(f"기준 값 : {n} - 5% 값 {five_percent_value} : {n - five_percent_value}")
        print(f"기준 값 : {n} + 5% 값 {five_percent_value} : {n + five_percent_value}")
        # ±5% 주식 값을 벗어난 값이 1분동안 지속된 경우 = ★이 된다.
        if is_remain_one_minute:
            if int(stock_values[i]) < (n - five_percent_value) or int(stock_values[i]) > (n + five_percent_value):
                print(datetime.time(current_stock_hour, current_stock_minute + 1, current_stock_second))
                flag = True  # 주식이 ★이 되는 구간이 있으므로 no value를 출력할 필요가 없음.
                break

if not flag:
    print("no value")
