# 2번 - 복권 당첨 평균

def get_lotto_avg(lottos):
    lotto_results = {}
    lottos.sort(key=lambda x: x[0])
    win_lotto_results = []

    for member_idx, lotto_result in lottos:
        if member_idx in lotto_results.keys():
            lotto_results[member_idx].append(lotto_result)
        else:
            lotto_results[member_idx] = [lotto_result]

    print("lotto hash map : ", lotto_results)

    for i in lotto_results.values():
        win_lotto_results.append(i.index(1) + 1)

    print('복권 당첨 평균 : ', sum(win_lotto_results) // len(lotto_results.keys()))
    return sum(win_lotto_results) // len(lotto_results.keys())


get_lotto_avg([[1, 0], [35, 0], [1, 0], [100, 1], [35, 1], [100, 1], [35, 1], [1, 1], [1, 1]])
