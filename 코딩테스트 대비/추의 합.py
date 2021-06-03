'''
 2g, 3g, 5g의 추 10개를 이용하여 추의 합이 만족되는 경우를 구하여 출력한다.

▶ 처리 조건
1) 각각 2g, 3g, 5g의 추 10개를 이용하여 추의 합이 만족되는 경우를 구하여 출력한다.
2) 각각의 추는 반드시 1개는 사용해야 한다.
3) 입력받은 그램과 2g, 3g, 5g의 추를 합산한 값이 일치하는 경우를 모두 구하고 그 경우의 수도 구한다.

▶ 입력 형식
1) 키보드를 이용하여 원하는 그램을 입력받는다.
2) 입력된 그램이 0이면 프로그램을 종료한다.
3) 그램의 입력범위는 10에서 100인 자연수이다.
4) 작업을 반복 수행한다.

▶ 출력 형식
1) 2g, 3g, 5g이 만족되는 경우를 출력하고, 맨 마지막 오른쪽에 총 경우의 수를 구하여 출력한다.
2) 입력범위를 벗어나는 자연수가 입력되면 ‘INPUT ERROR! (DATA RANGE 10 - 100)’을 출력 후 재입력 받는다.

▶ 입력과 출력의 예
원하는 그램을 입력하세요 : 31
2g 3g 5g
1 3 4
1 8 3
2 4 3
3 5 2
4 1 4
4 6 1
5 2 3
6 3 2
7 4 1
9 1 2
10 2 1
경우의 수 = 11가지

원하는 그램을 입력하세요 : 38
2g 3g 5g
1 2 6
1 7 3
2 3 5
2 8 2
3 4 4
3 9 1
4 5 3
5 1 5
5 6 2
6 2 4
6 7 1
7 3 3
8 4 2
9 5 1
10 1 3
경우의 수 = 15가지

원하는 그램을 입력하세요 : 138
INPUT ERROR! (DATA RANGE 10 - 100)

원하는 그램을 입력하세요 : 0

'''
while True:
    gram = int(input())
    result = []

    if gram < 10 or gram > 100:
        print("INPUT ERROR! (DATA RANGE 10 - 100)")
        continue

    for i in range(1, gram):
        for j in range(1, gram):
            for k in range(1, gram):
                if (i * 2) + (j * 3) + (k * 5) == gram:
                    result.append([i, j, k])

    result = [i for i in result if len(list(filter(lambda gram: gram <= 10, i))) >= 3]
    print(len(result))
