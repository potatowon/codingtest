import sys

round = int(input())

for _ in range(round):
    A = list(map(str, sys.stdin.readline().split()))
    B = list(map(str, sys.stdin.readline().split()))
    a = A[1:]
    b = B[1:]

    if a.count('4') > b.count('4'):
        print('A')
        continue
    elif a.count('4') < b.count('4'):
        print('B')

        continue
    else:
        if a.count('3') > b.count('3'):
            print('A')
            continue
        elif a.count('3') < b.count('3'):
            print('B')
            continue
        else:
            if a.count('2') > b.count('2'):
                print('A')
                continue
            elif a.count('2') < b.count('2'):
                print('B')
                continue
            else:
                if a.count('1') > b.count('1'):
                    print('A')
                    continue
                elif a.count('1') < b.count('1'):
                    print('B')
                    continue
                else:
                    print('D')
                    continue

