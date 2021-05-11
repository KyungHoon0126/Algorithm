word = input()


def is_palindrome1(word):
    is_palindrome = True  # 회문 판별값을 저장할 변수, 초깃값은 True
    for i in range(len(word) // 2):  # 0부터 문자열 길이의 절반만큼 반복
        if word[i] != word[-1 - i]:  # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
            is_palindrome = False  # 회문이 아님
            break
    return is_palindrome


def is_palindrome2(word):
    for i in range(len(word) // 2):
        if word[i] != word[-1 - i]:
            return False
    return True


print(word)
print(word[::-1])
print(''.join(reversed(word)))
print('is_palindrome1', is_palindrome1(word))
print('is_palindrome2', is_palindrome2(word))
