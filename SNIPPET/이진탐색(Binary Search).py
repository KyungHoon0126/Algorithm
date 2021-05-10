# target : 찾고자 하는 값
# data : 오름차순으로 정렬된 리스트
# start : data의 처음 값 인덱스
# end : data의 마지막 값 인덱스
# mid : start, end의 중간 인덱스

def binary_search(target, data):
    data.sort()
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None


data = [4, 1, 5, 2, 3]

print(data)
idx = binary_search(1, data)
print('위치 : ', idx)