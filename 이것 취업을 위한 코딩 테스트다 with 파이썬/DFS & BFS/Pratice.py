# Stack
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)

stack.pop()

stack.append(1)
stack.append(4)
stack.pop()

print("Stack Asc : ", stack)
print("Stack Desc : ", stack[::-1])

# Queue
from collections import deque

# 큐(Queue) 구현을 위한 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)

queue.popleft()

queue.append(1)
queue.append(4)

queue.popleft()

print("Queue Asc : ", queue)
queue.reverse()
print("Queue Desc", queue)

print("List Queue : : ", list(queue))


# 재귀 함수
# def recursive_function():
#     print('재귀 함수를 호출합니다.')
#     recursive_function()
#
#
# recursive_function()

def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i + 1, '번째 쟂귀 함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀 함수를 종료합니다.')


recursive_function(1)


# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result


# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:  # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n - 1)


# 각각의 방식으로 구현한 n! 출력(n = 5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))

# DFS : Depth-First Search, 깊이 우선 탐색
# 그래프 표현 방식
# 1) 인접 행렬 : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
# 2) 인접 리스트 : 리스트로 그래프의 연결 관계르 표현하는 방식
INF = 999999999  # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print("인접 행렬 : ", graph)

# 2차원 리스트를 이용해 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0, 5))

print("인접 리스트 : ", graph)