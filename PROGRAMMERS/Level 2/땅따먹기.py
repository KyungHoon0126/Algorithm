def solution(land):
    answer = 0

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            # land[i][j] + 그 위에 줄의 j열 빼고 만든 리스트에서 max값을 뽑아서 더해주라는 뜻.
            # land[i - 1][:j]를 하면 j열 앞까지 리스트가 뽑히고 land[i - 1][j + 1:]을 하면 j + 1열부터 끝까지 리스트가 뽑혀서
            # 리스트끼리 더하면 합쳐진 리스트가 된다. 이 리스트에서 max 값을 더해준다.
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])
    return max(land[len(land) - 1])


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))  # 16
