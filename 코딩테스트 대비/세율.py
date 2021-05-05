# 1번 - 세율
import copy

money = int(input())  # 50000000
tax = 0
calculated_money = copy.deepcopy(money)

money_types = {
    "TWELVE_MILLION_WON": 12000000,  # 일천이백만원
    "FORTY-SIX_MILLION_WON": 46000000,  # 사천육백만원
    "EIGHTY-EIGHT_MILLION_WON": 88000000,  # 팔천팔백만원
    "ONE-HUNDRED-FIFTY_MILLION_WON": 150000000,  # 일억오천만원
    "THREE-HUNDRED_MILLION_WON": 300000000,  # 삼억원
    "FIVE-HUNDRED_MILLION_WON": 500000000  # 오억원
}


def get_money(type):
    return money_types[type]


# 1,200만원 이하
if money >= get_money("TWELVE_MILLION_WON"):
    # 현재 남은 금액이 1,200만원 이상인 경우
    if calculated_money >= get_money("TWELVE_MILLION_WON"):
        tax += (get_money("TWELVE_MILLION_WON") * 0.06)
        # 남은 금액 계산
        calculated_money -= get_money("TWELVE_MILLION_WON")
    # 현재 남은 금액이 1,200만원보다 작은 경우, 남은 금액에 대해서만 세금을 계산.
    else:
        tax += (calculated_money * 0.06)
        # 남은 금액 계산
        calculated_money -= calculated_money

# 1,200만원 초과 ~ 4,600만원 이하
if money > get_money("TWELVE_MILLION_WON") and money >= get_money("FORTY-SIX_MILLION_WON"):
    if calculated_money >= get_money("FORTY-SIX_MILLION_WON"):
        tax += 720000 + ((get_money("FORTY-SIX_MILLION_WON") - get_money("TWELVE_MILLION_WON")) * 0.15)
        calculated_money -= get_money("FORTY-SIX_MILLION_WON")
    else:
        tax += 720000 + (calculated_money * 0.15)
        calculated_money -= calculated_money

# 4,600만원 초과 ~ 8,800만원 이하
if money > get_money("FORTY-SIX_MILLION_WON") and money >= get_money("EIGHTY-EIGHT_MILLION_WON"):
    if calculated_money >= get_money("EIGHTY-EIGHT_MILLION_WON"):
        tax += 5820000 + ((get_money("EIGHTY-EIGHT_MILLION_WON") - get_money("FORTY-SIX_MILLION_WON")) * 0.24)
        calculated_money -= get_money("EIGHTY-EIGHT_MILLION_WON")
    else:
        tax += 5820000 + (calculated_money * 0.24)
        calculated_money -= calculated_money

# 8,800만원 초과 ~ 1억 5,000만원 이하
if money > get_money("EIGHTY-EIGHT_MILLION_WON") and money >= get_money("ONE-HUNDRED-FIFTY_MILLION_WON"):
    if calculated_money >= get_money("ONE-HUNDRED-FIFTY_MILLION_WON"):
        tax += 15900000 + ((get_money("ONE-HUNDRED-FIFTY_MILLION_WON") - get_money("EIGHTY-EIGHT_MILLION_WON")) * 0.35)
        calculated_money -= get_money("ONE-HUNDRED-FIFTY_MILLION_WON")
    else:
        tax += 15900000 + (calculated_money * 0.35)
        calculated_money -= calculated_money

# 1억 5,000만원 초과 ~ 3억원 이하
if money > get_money("ONE-HUNDRED-FIFTY_MILLION_WON") and money >= get_money("THREE-HUNDRED_MILLION_WON"):
    if calculated_money >= get_money("THREE-HUNDRED_MILLION_WON"):
        tax += 37600000 + ((get_money("THREE-HUNDRED_MILLION_WON") - get_money("ONE-HUNDRED-FIFTY_MILLION_WON")) * 0.38)
        calculated_money -= get_money("THREE-HUNDRED_MILLION_WON")
    else:
        tax += 37600000 + (calculated_money * 0.38)
        calculated_money -= calculated_money

# 3억원 초과 ~ 5억원 이하
if money > get_money("THREE-HUNDRED_MILLION_WON") and money >= get_money("FIVE-HUNDRED_MILLION_WON"):
    if calculated_money >= get_money("FIVE-HUNDRED_MILLION_WON"):
        tax += 94600000 + ((get_money("FIVE-HUNDRED_MILLION_WON") - get_money("THREE-HUNDRED_MILLION_WON")) * 0.40)
        calculated_money -= get_money("FIVE-HUNDRED_MILLION_WON")
    else:
        tax += 94600000 + (calculated_money * 0.40)
        calculated_money -= calculated_money

# 5억원 초과
if money > get_money("FIVE-HUNDRED_MILLION_WON"):
    if calculated_money > get_money("FIVE-HUNDRED_MILLION_WON"):
        tax += 174600000 + ((get_money("FIVE-HUNDRED_MILLION_WON") - get_money("THREE-HUNDRED_MILLION_WON")) * 0.42)
        calculated_money -= get_money("FIVE-HUNDRED_MILLION_WON")
    else:
        tax += 174600000 + (calculated_money * 0.42)
        calculated_money -= calculated_money

print(f'내야할 세금은 {round(tax)}원 입니다.')
