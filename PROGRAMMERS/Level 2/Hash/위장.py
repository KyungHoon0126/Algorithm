# Hash - 위장

def solution(clothes):
    answer = 1
    hash_map = {}  # 중복 허용 X, 키 값이 같은 경우 마지막 값이 들어감.

    # clotehs[의상 이름, 의상 종류] -> clotehs[value, key] 형식으로 이루어져 있음.
    for val, key in clothes:
        if key in hash_map.keys():
            hash_map[key].append(val)
        else:
            # hash_map[key] = val
            # []로 감싸서 넣어주는 이유는 같은 key의 value가 있을 경우 append 해야하기 때문에 []로 감싸준다.
            hash_map[key] = [val]

    for val in hash_map.values():
        # 각 부위(key)에서 착용할 수 있는 옷의 개수 + 안 입을 경우(1)
        answer *= (len(val) + 1)

    # 하루에 최소 한 개의 의상은 입으므로 answer - 1
    return answer - 1


solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])  # 5
# solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]) # 3
