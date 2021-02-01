# N X M 크기의 2차원 리스트 초기화
n = 3
m = 3
array = [[0] * m for _ in range(n)]

print(array)

dx = [0, -1, 0, 1]  # 행, 세로
dy = [1, 0, -1, 0]  # 열, 가로

x, y = 1, 1

cnt = 1

for i in range(4):
    ''' case1   
    nx = x + dx[i]
    ny = y + dy[i]
    array[nx][ny] = cnt
    print(f"{cnt} 넣을 위치는 {nx + 1}행 {ny + 1}열 입니다.")
    '''

    #  case2
    array[x + dx[i]][y + dy[i]] = cnt
    print(f"{cnt} 넣을 위치는 {x + dx[i] + 1}행 {y + dy[i] + 1}열 입니다.")

    cnt += 1

for i in array:
    for j in i:
        print(j, end=' ')  # end : 문장을 출력하고 마지막에 무엇을 쓰고 끝낼지 정할 수 있다.
    print()
