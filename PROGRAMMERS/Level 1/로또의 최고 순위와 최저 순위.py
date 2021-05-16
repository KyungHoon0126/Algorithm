def get_ranking(cnt):
    if cnt == 6:
        return 1
    elif cnt == 5:
        return 2
    elif cnt == 4:
        return 3
    elif cnt == 3:
        return 4
    elif cnt == 2:
        return 5
    else:
        return 6


def solution(lottos, win_nums):
    answer = []

    win_cnt = 0
    zero_cnt = 0

    for lotto in lottos:
        if lotto in win_nums:
            win_cnt += 1
        elif lotto == 0:
            zero_cnt += 1

    # 최고 순위
    answer.append(get_ranking(win_cnt + zero_cnt))

    # 최저 순위
    answer.append(get_ranking(win_cnt))

    return answer
