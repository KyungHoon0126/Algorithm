
# 정렬 - H-Index

def solution(citations):
    citations.sort()
    num = len(citations)  # 발표한 논문 개수(가장 큰 h 값을 구하고 싶기 때문에 최댓값부터 시작.)

    while True:
        for idx, value in enumerate(citations):
            if value >= num and len(citations[idx:]) >= num:
                return num
        else:
            num -= 1
            continue
        break