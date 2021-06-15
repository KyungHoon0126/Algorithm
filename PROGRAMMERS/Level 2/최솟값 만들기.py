def solution1(A, B):
    A.sort()
    B.sort(reverse=True)
    return sum([a * b for a, b in zip(A, B)])


def solution2(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])
