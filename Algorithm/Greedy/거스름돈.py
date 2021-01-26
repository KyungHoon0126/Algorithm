'''
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)
'''

n = int(input())
count = 0

coin_types = [500, 100, 50, 10]  # 큰 단위의 화폐부터 차례대로 확인

coin_counts = []  # 각 화폐의 수 저장

for coin in coin_types:
    count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    coin_counts.append(n // coin)
    n %= coin

print(f"최소 동전 개수 : {count}개")

idx = 0

for coin in coin_types:
    if idx == 4:
        break
    print(f"{coin}원 동전 개수 : {coin_counts[idx]}개")
    idx += 1
