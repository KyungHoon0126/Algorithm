
# 힙 - 디스크 컨트롤러

import heapq

def solution(jobs):
    jobs_len = len(jobs)
    time, end, queue = 0, -1, []
    count = 0 # 처리한 프로세스 개수
    answer = 0

    # time : 오로지 프로세스의 수행시간과 다음 프로세스 시작 전 시간 간격의 합. / answer : 대기시간과 프로세스 수행시간의 총합.

    while count < jobs_len:
        # i[0] : 프로세스 입력 시간, i[1] : 프로세스가 끝날 때까지 걸리는 시간
        for i in jobs:
            if end < i[0] <= time:
                # 현재 시간 기준, 프로세스가 queue에 들어가서 얼마나 기다렸는지를 더함. (대기시간)
                answer += (time - i[0])
                # 프로세스가 끝날 때까지 걸리는 시간을 queue에 넣어준다.
                heapq.heappush(queue, i[1])

        if len(queue) > 0:
            # 가장 빨리 끝나는 프로세스가 끝날 때까지 걸린 시간을 더함.
            answer += len(queue) * queue[0]
            end = time
            # 가장 빨리 끝나는 프로세스가 걸린 시간을 더해준다.
            time += heapq.heappop(queue)
            # 프로세스가 끝났으므로 count +1 해준다.
            count += 1
        # queue에 아직 아무것도 없다면 시간을 +1 해준다.
        else:
            time += 1

    return int(answer / jobs_len)




































