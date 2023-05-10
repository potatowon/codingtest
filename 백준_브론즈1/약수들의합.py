import sys

while True:
    num = int(sys.stdin.readline())
    digit = []
    if num == -1:
        break

    else:
        tmp = 0
        for i in range(1, num):
            if num % i == 0:
               tmp += i
               digit.append(str(i))
        if tmp == num:
            print(f'{num} = ' + ' + '.join(digit))
        else:
            print(f'{num} is NOT perfect.')


