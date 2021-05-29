def solution(record):
    answer = []
    dict = {}

    # 닉네임 처리
    for i in record:
        i = i.split(' ')
        if i[0] == 'Enter' or i[0] == 'Change':
            dict[i[1]] = i[2]

    # 입장·퇴장 여부에 따른 출력
    for i in record:
        i = i.split()
        if i[0] == 'Enter':
            answer.append(f"{dict[i[1]]}님이 들어왔습니다.")
        elif i[0] == 'Leave':
            answer.append(f"{dict[i[1]]}님이 나갔습니다.")

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
