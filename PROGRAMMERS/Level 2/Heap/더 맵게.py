import heapq

# 힙 - 더 맵게

def solution(scoville, K):
    heap = []
    for value in scoville:
        heapq.heappush(heap, value)

    print(heap)

    mix_cnt = 0
    # 여기서 min(heap) 대신 heap[0]을 사용하는 이유는 heapq는 push, pop 할때마다 자동으로 정렬해주기 때문.
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        mix_cnt += 1

    return mix_cnt


solution([1, 2, 3, 9, 10, 12], 7)
