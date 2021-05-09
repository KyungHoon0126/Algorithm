numbers = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "twenty-one": 21, "twenty-two": 22, "twenty-three": 23, "twenty-four": 24, "twenty-five": 25,
    "twenty-six": 26, "twenty-seven": 27, "twenty-eight": 28, "twenty-nine": 29, "thirty": 30,
    "thirty-one": 31, "thirty-two": 32, "thirty-three": 33, "thirty-four": 34, "thirty-five": 35,
    "thirty-six": 36, "thirty-seven": 37, "thirty-eight": 38, "thirty-nine": 39, "forty": 40,
    "forty-one": 41, "forty-two": 42, "forty-three": 43, "forty-four": 44, "forty-five": 45,
}

reverse_numbers = dict(map(reversed, numbers.items()))


def get_time(hour):
    return reverse_numbers.get(int(hour))


# 시간 범위 : 1 ~ 12 / 분 범위 : 0 ~ 59

hour, minute = input().split(':')

# 분은 항상 두 자리이므로 한 자리일 경우  zfill()로 자리를 맞추어 준다.
if len(minute) < 2:
    minute = minute.zfill(2)

if minute == '00':
    print(f'{get_time(hour).title()} o''clock')
if minute == '15':
    print(f'Quarter past {get_time(hour)}')
if minute == '30':
    print(f'{get_time(hour).title()} thirty')
if minute == '45':
    print(f'Quarter to {get_time(int(hour) + 1)}')
if int(minute) < 45:
    print(f'{get_time(hour).title()} {get_time(minute)}')
if int(minute) > 45:
    print(f'{get_time(60 - int(minute)).title()} to {get_time(int(hour) + 1)}')
