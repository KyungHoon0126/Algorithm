def solution(skill, skill_trees):
    answer = 0
    skills = [i for i in skill]  # ex) skill = "CBD"의 문자열을 각 요소별로 분리.
    skill_trees_len = len(skill_trees)
    data = [[] * skill_trees_len for _ in range(skill_trees_len)]  # skill_trees의 크기와 동일한 2차원 배열 생성.

    # skills에 각 문자열로 나누어 놓은 각 skill의 위치를 data 2차원 배열에 저장.
    for idx, skill_tree in enumerate(skill_trees):
        for skill in skills:
            if skill in skill_tree:
                data[idx].append(skill_tree.find(skill))
                data[idx].sort()

    # skill_trees의 각 skill위치를 저장한 순서대로 조합한 skill 문자를 저장하기 위한 배열.
    completed_skills = []

    # skill_trees의 각 skill위치를 저장한 순서대로 skill 문자 조합.
    for skill_tree, val in zip(skill_trees, data):  # skill_trees의 각 요소와 각 요소별 skill 위치를 zip을 통해 묶어준다.
        temp = ''
        for i in val:
            temp += skill_tree[i]
        completed_skills.append(temp)
        temp = ''

    # 조합한 문자열과 skill 순서대로 맞는지 확인
    for com_skill in completed_skills:
        # 완성된 각 스킬(com_skill)의 길이만큼 skill을 잘라서 비교
        if com_skill == ''.join(skills)[0:len(com_skill)]:
            answer += 1

    return answer
