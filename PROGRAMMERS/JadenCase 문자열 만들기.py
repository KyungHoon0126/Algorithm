def solution(s):
    s = s.split(' ')
    for i in range(len(s)):
        # capitalize() : 첫 문자가 알파벳일 경우 대문자로 만들고, 두번째 문자부터는 자동으로 소문자로 만든다.
        # 단, 첫 문자가 알파벳이 아니면 그대로 리턴한다
        s[i] = s[i].capitalize()
    return ' '.join(s)
