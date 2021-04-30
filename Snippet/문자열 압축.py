s = "aaabbcccccca"
result = s[0] # 문자가 앞, 숫자가 뒤
answer = '' # 문자가 뒤, 숫자가 앞
count = 0

for i in s:
    if i == result[-1]:
        count += 1
    else:
        result += str(count) + i
        count = 1

result += str(count)

print(result) # a3b2c6a1

print(result[0::2]) # 짝수 인덱스만 추출, 0부터 시작하고 2씩 증가
print(result[1::2]) # 홀수 인덱스만 추출, 1부터 시작하고 2씩 증가

for i in zip(result[1::2], result[0::2]):
    answer += ''.join(map(str, i))

print(answer) # 3a2b6c1a