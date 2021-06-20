'''
▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
'''


# 참고 사이트 : https://bellog.tistory.com/152

# 조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
# ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

# 풀이 : 크게 두 가지 방향에서 최솟값 고려
# 첫 번째 : 상, 하 방향의 관점. A부터 오름차순으로 알파벳을 찾는게 빠른지, Z부터 내림차순으로 찾는 게 빠른지 비교
# 두 번째 : 좌, 우 방향의 관점. A로만 이루어진 상태에서 문자열을 찾기 때문에 마지막 남은 문자열이 연속된 A라면 이동하지 않고 완성가능.
#          따라서 왼쪽에서 오른쪽으로만 이동하는 일반적인 경우와 움직이는 횟수와 반대 방향으로 이동하는 경우의 움직이는 횟수를 비교해 최솟값을 찾는다.

def solution(name):
    answer = 0
    min_move = len(name) - 1
    next = 0

    # A부터 오름차순으로 알파벳을 찾는 것이 빠른지, 아니면 Z부터 내림차순으로 찾는 것이 빠른지 비교.
    # 문자열에 속한 알파벳들을 차례로 탐색해 최솟값을 찾아 answer에 더해 나간다. 해당 문자가 A인 경우는 0, Z인 경우는 1
    for idx, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        next = idx + 1

        # next가 전체 길이보다 작고 next가 'A'일때까지 최소 이동 값 계산
        # 즉 A가 나오기 전까지 왼쪽에서 오른쪽으로 이동하다가 A를 만나면 온만큼 되돌아 간다.
        # 그 다음 문자열의 끝으로 돌아서 A가 나오기 전까지 이동한다.
        while next < len(name) and name[next] == 'A':
            next += 1  # 연속된 A 구간의 마지막 A의 인덱스를 가리킨다.

        # min_move와 (A가 나오기 전까지 왼쪽에서 오른쪽으로 이동한 횟수 + A를 만나 온만큼 돌아간 횟수 + 전체길이에서 마지막 A의 인덱스 값을 뺀 수)의 최솟값
        min_move = min(min_move, idx + idx + len(name) - next)

    answer += min_move

    return answer


print(solution("JEROEN"))  # 56
# print(solution("JAN"))  # 23
