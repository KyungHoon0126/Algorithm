def solution(N, stages):
    peoples = len(stages)
    failure_rates = {}

    for num in range(1, N + 1):
      failures = peoples - len([i for i in stages if i > num])
      if peoples == 0:
         failure_rates[num] = 0
         continue
      failure_rates[num] = failures / peoples
      peoples -= failures

    failure_rates = sorted(failure_rates.items(), key=lambda x: (-x[1], x[0]))

    return [i[0] for i in failure_rates]