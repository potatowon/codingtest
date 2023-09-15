equation = input().rstrip()
equation = equation.split("-")
res = []

for eq in equation:
    if '+' in eq:
        # +로 나뉜 각각의 값을 정수로 변환하여 합산
        res.append(sum(map(int, eq.split('+'))))
    else:
        res.append(int(eq))

answer = res[0]
for i in res[1:]:
    answer -= i

print(answer)
