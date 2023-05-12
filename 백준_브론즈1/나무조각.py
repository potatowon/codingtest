number = list(map(int, input().split()))
answer = sorted(number)

while True:
    for idx, n in enumerate(number):
        if idx > 0 and n < number[idx-1]:
            number[idx], number[idx-1] = number[idx-1], number[idx]
            print(*number)
    if answer == number:
        break