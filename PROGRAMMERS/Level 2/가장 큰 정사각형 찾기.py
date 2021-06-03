# 파이썬
import itertools
import numpy as np


def solution(board):
    H, W = len(board), len(board[0])  # 4, 4

    for i in range(1, H):
        for j in range(1, W):
            if board[i][j] == 1:
                # (1, 1)자리 기준, 대각선, 위쪽, 왼쪽 3가지를 만족하면 정사각형이 된다. 이들의 최솟값에 1을 더해준다.
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1
                print(np.array(board))

    print(list(itertools.chain(*board)))

    # board를 itertools.chain()으로 합친다음 max를 찾아 제곱
    return max(itertools.chain(*board)) ** 2


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))  # 9
