import sys

input = sys.stdin.readline


def is_palindrome(a, primes):
    answer = []

    for prime in primes:
        if len(str(prime)) <= 1 and prime >= a:
            answer.append(prime)

    for prime in primes:
        for i in range(len(str(prime)) // 2):
            if str(prime)[i] != str(prime)[-1 - i]:
                break
            else:
                answer.append(prime)
    return answer


def get_primes(b):
    answer = set(range(2, b + 1))
    for i in range(2, b + 1):
        if i in answer:
            answer -= set(range(i * 2, b + 1, i))
    return answer


a, b = map(int, input().split())

print(is_palindrome(a, get_primes(b)))
