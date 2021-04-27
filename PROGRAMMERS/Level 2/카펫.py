# 노란색 카펫을 감싸는 전체 갈색 카펫의 크기(노란색 카펫을 감싸는 둘레) = (가로 + 세로) * 2 - 4 = brown
# -4를 해주는 이유는 각 변의 길이를 4번 더할 때 생기는 공통부분 모서리 부분 길이 제거

# 노란색 카펫의 크기 = (가로 - 2) * (세로 - 2) = yellow
# 가로, 세로의 최대 길이 = 네 변의 최대합의 길이 // 2 = brown // 2

def solution(brown, yellow):
    answer = []
    max_carpet_len = brown // 2
    # 노란색 카펫 1개일 때 최소 갈색 카펫의 개수는 9 => 3 x 3이므로 가로와 세로 모두 3부터 시작.
    for h in range(3, max_carpet_len):
        for w in range(3, max_carpet_len):
            if (h + w) * 2 - 4 == brown and (h - 2) * (w - 2) == yellow:
                return [w, h]
    return answer