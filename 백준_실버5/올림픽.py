n, k = map(int, input().split())

countries = []

# 각 국가의 메달 정보를 튜플로 저장
for _ in range(n):
    country, gold, silver, bronze = map(int, input().split())
    countries.append((country, (gold, silver, bronze)))

# 메달 정보로 정렬 (내림차순)
countries.sort(key=lambda x: x[1], reverse=True)

# K 국가의 메달 정보 찾기
k_medals = None
for country, medals in countries:
    if country == k:
        k_medals = medals
        break

# K 국가의 등수 계산
rank = 1
for _, medals in countries:
    if medals == k_medals:
        break
    rank += 1

print(rank)
'''
메달의 수가 매우 클 수도 있다는 점을 감안할 때, 이 방법은 여전히 문제가 있을 수 있습니다. 또한, 이 방법은 메달 수를 단일 수치로 변환하는 접근 방법이며, 이는 사실상 필요하지 않습니다.
좀 더 효과적인 방법은 각 국가의 메달 수를 튜플로 유지하고, 튜플을 비교하여 정렬하는 것입니다. 튜플을 비교할 때, 파이썬은 첫 번째 요소를 먼저 비교하고, 이들이 같으면 두 번째 요소를 비교하고, 그 다음은 세 번째 요소를 비교합니다. 이는 문제에서 요구하는 대로 금메달, 은메달, 동메달 순으로 비교하는 것과 일치합니다.
다음은 수정된 코드입니다:
'''



