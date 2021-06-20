# https://gurumee92.tistory.com/162

def solution1(number, k):
    collected = []

    for idx, num in enumerate(number):
        # collected에 원소가 있고, 마지막 원소가 순회 수 num보다 작고, k가 0보다 크다면
        while collected and collected[-1] < num and k > 0:
            # collected의 가장 맨 뒤의 원소를 제거.
            collected.pop()
            # k를 감소.
            k -= 1

        # k가 0이라면 더 이상 뺄 수 있는 수가 없으므로 현재 인덱스 부터 끝까지 collected를 이어 붙인다.
        if k == 0:
            collected += number[idx:]
            break

        # 순회수 num을 collected에 넣어준다.
        collected.append(num)

    # k가 0보다 크다면(k가 남은 경우) collected를 뒤에서 k개 만큼 자른다.
    collected = collected[:-k] if k > 0 else collected
    answer = ''.join(collected)
    print(answer)
    return answer


# solution1("1924", 2)
# solution1("1231234", 3)
solution1("4177252841", 4)


# 스택을 활용한 풀이

def solution2(number, k):
    # 1. 스택 생성
    st = []

    # 2. 큰 수가 앞자리가 되게끔 스택에 저장.
    for elem in number:
        while st and st[-1] < elem and k > 0:
            st.pop()
            k -= 1

        st.append(elem)

    # 3. k가 남았다면 뒤에서부터 뺀다.
    while k > 0:
        st.pop()
        k -= 1

    answer = "".join(st)
    return answer
