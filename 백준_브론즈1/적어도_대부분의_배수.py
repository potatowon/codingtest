num = list(map(int, input().split()))
result = min(num)

while True:
    cnt = sum([1 for i in num if result%i == 0])
    if cnt >= 3:
        print(result)
        break
    result += 1