
# (점수/Max)*100
# 위 방법으로 계산한 새로운 평균을 구하시오



n_scores = int(input())
scores = list(map(int, input().split(' ')))

new_score = [(n/max(scores))*100 for n in scores]
print(sum(new_score)/n_scores)