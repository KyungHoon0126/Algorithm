math_giver_answers = [[1, 2, 3, 4, 5],
                      [2, 1, 2, 3, 2, 4, 2, 5],
                      [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

scores = [0, 0, 0]

def solution(answers):

  answer = []

  for i in range(len(answers)):
    if answers[i] == math_giver_answers[0][i % 5]:
      scores[0] += 1
    if answers[i] == math_giver_answers[1][i % 8]:
      scores[1] += 1
    if answers[i] == math_giver_answers[2][i % 10]:
      scores[2] += 1

  for idx, score in enumerate(scores):
    if score == max(scores):
      answer.append(idx + 1)

  return answer

solution([1,2,3,4,5])