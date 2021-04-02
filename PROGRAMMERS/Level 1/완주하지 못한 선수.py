def solution(participant, completion):
    participant.sort()
    completion.sort()

    print(zip(participant, completion))

    for i in completion:
        if i in participant:
            participant.remove(i)
    return ''.join(participant)


# solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
# solution(["leo", "kiki", "eden"], ["eden", "kiki"])
solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])