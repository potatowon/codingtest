start, end = map(int, input().split())
answer = []
for i in range(1, 51):
    answer += [i]*i

print(sum(answer[start-1:end]))
