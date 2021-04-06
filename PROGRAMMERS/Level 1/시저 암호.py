def solution(s, n):
    answer = ''
    for i in list(s):
      if (i == ' '):
        answer += ' '
      elif ord(i) >= 65 and ord(i) <= 90:
        if ord(i) + n > 90:
          answer += chr(ord(i) -1 -25 + n)
        else:
          answer += chr(ord(i) + n)
      elif ord(i) + n > 122:
        answer += chr(ord(i) -1 -25 + n)
      else:
        answer += chr(ord(i) + n)
    return answer

solution("a B z", 4)