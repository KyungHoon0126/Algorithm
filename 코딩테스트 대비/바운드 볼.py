'''
바운드 볼

번호가 적힌 N개의 공을 바구니에 넣고 K개 만큼 빼기를 반복할 것이다.
이 때 마지막에 바구니에 남은 공의 번호를 출력하시오.
단 바구니의 깊이는 10000미만이다.

첫 줄에는 총 횟수를 입력받는다
둘째 줄에는 바구니에 넣을 N개(1<=N<=100)의 공 번호를 입력받는다.
셋째 줄에는 바구니에서 뺄 공의 개수를 입력받는다.(2면 2개를 뺀다)
그 다음번 줄부터는 총 횟수만큼 2,3번 줄의 형태를 반복한다.

입력
2
1 2 3
2
2 3 4 5
1

출력
1 2 3 4

입력
2
5 3 8 9
3
6 8 3
1

출력
5 6 8


입력
2
1 2 3
2
1 2 3
0

출력
1 1 2 3
'''

bound_balls = []

for i in range(int(input('총 횟수를 입력해 주세요 : '))):
    numbers = list(map(int, input('바구니에 넣을 공 번호를 입력해 주세요 : ').split()))
    cnt = int(input('바구니에서 뺄 공의 개수를 입력해 주세요 : '))

    numbers = numbers[0:len(numbers) - cnt]
    bound_balls = bound_balls + numbers

print(' '.join(map(str, bound_balls)))
