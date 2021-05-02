# 문자열 압축

def solution(s):
    # 문자열 길이로 초기화, 최대값은 문자열 길이이기 때문.
    answer = len(s)
    # 분할 단위로 나누었을 때 문자열의 길이가 같아야 하는데, 그 최대 길이는 전체 문자열의 절반이므로 len(s) // 2 + 1까지 반복.
    for i in range(1, len(s) // 2 + 1):
        # 몇 번째, 어느 위치에서 문자열을 처리하고 있는지 표현하는 변수.
        pos = 0

        # 압축되었을 때의 길이
        length = len(s)  # 문자열 길이로 초기화

        # 위치를 기준으로 압축하고자 하는 길이만큼 문자열을 얻어오는데 문자열 길이 끝까지 반복.
        while pos + i <= len(s):
            # 압축하고자 하는 단위만큼 문자열을 얻어옴.
            unit = s[pos:pos + i]  # a, ab, aba
            print('unit1', unit)
            pos += i
            # 몇 번 반복 되었는지 계산.
            cnt = 0

            while pos + i <= len(s):
                # 만약 i가 2라고 가정하면, 현재 unit = ab, 이 unit의 단위만큼 문자열을 비교.
                if unit == s[pos:pos + i]:
                    print('unit2', unit)
                    cnt += 1
                    pos += i
                else:
                    break

            # 반복된게 있다면, 문자열이 압축되었다는 것.
            if cnt > 0:
                print('cnt', cnt)
                print('length', length)
                
                # 반복된 횟수만큼 문자열을 빼주고 숫자를 적어줘야 함.
                length -= i * cnt 

                # 문자 앞에 반복된 횟수를 적는데 자릿수 마다 일의 자리, 십의 자리, 백의자리 ···
                # 이렇게 늘어나기 때문에 자릿수 마다 다르게 길이를 증가
                if cnt < 9:
                    length += 1
                elif cnt < 99:
                    length += 2
                elif cnt < 999:
                    length += 3
                else:
                    length += 4

        answer = min(answer, length)
    print(answer)
    return answer


test_case = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]
for i in test_case:
    solution(i)
