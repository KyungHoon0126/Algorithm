def solution(board, moves):
    array = [[] * len(board[0]) for _ in range(len(board[0]))]  # 새롭게 만든 인형 배치도
    results = []  # 뽑기 결과 비교를 위한 배열
    answer = 0  # 터트려져 사라잔 인형 개수

    # 인형위치 재배열
    for i in board:
        for idx, j in enumerate(i):
            if j != 0:
                array[idx].append(j)

    # 초기 뽑기 값 설정
    results.append(array[moves[0] - 1][0])
    del array[moves[0] - 1][0]
    del moves[0]

    # 뽑기 진행
    for i in range(0, len(moves)):
        for j in moves:
            if len(array[j - 1]) > 0:
                # 해당 위치에 인형은 있으나, 아직 인형을 뽑지 않은 경우
                if len(results) < 1:
                    results.append(array[j - 1][0])
                    del array[j - 1][0]
                    moves.remove(j)
                    break
                # 이미 뽑아 놓은 인형이 있는 상태에서, 현재 뽑은 인형이 같은 경우
                if results[-1] == array[j - 1][0]:
                    answer += 2
                    del results[-1]
                    del array[j - 1][0]
                    moves.remove(j)
                    break
                else:
                    results.append(array[j - 1][0])
                    del array[j - 1][0]
                    moves.remove(j)
                    break
            # 뽑기를 진행했으나, 해당 위치에 인형이 없는 경우
            else:
                moves.remove(j)
                break

    return answer


# solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1, 5, 3, 5, 1, 2, 1, 4])
solution([[0,0,0,0,0], [0,0,1,0,3], [0,2,5,0,1], [4,2,4,4,2], [3,5,1,3,1]], [1,5,3,5,1,2,5,1,4,3])