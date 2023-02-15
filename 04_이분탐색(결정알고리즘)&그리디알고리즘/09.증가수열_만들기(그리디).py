'''
모두 자연수로 구성된 길이 N 의 수열

왼쪽 맨 끝 또는 오른쪽 맨끝 하나를 가져와 나열하여 가장 긴 증가수열을 만든다.

1. 증가 수열의 최대길이
2. 가져간 순서대로 LR 출력
'''


import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

rt = -1
lt = 0
answer = ''
result = []
d = 0
while True:
    if numbers[lt] < numbers[rt]:
        if numbers[lt] > d:
            d = numbers.pop(0)
            result.append(d)
            answer += "L"
        elif numbers[rt] > d:
            d = numbers.pop()
            result.append(d)
            answer += "R"
        else:
            break

    elif numbers[lt] > numbers[rt]:
        if numbers[rt] > d:
            d = numbers.pop()
            result.append(d)
            answer += "R"
        elif numbers[lt] > d:
            d = numbers.pop(0)
            result.append(d)
            answer += 'L'
        else:
            break
    else:
        break
print(len(result))
print(answer)

