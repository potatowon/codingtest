def backTracking(idx, tot):
    global minAns
    global maxAns
    if idx == n-1:
        if minAns > tot:
            minAns = tot
        if maxAns < tot:
            maxAns = tot
        return

    for i in range(4):
        temp = tot
        if operators[i] == 0:
            continue
        if i == 0:
            tot += numArr[idx + 1]
        elif i == 1:
            tot -= numArr[idx + 1]
        elif i == 2:
            tot *= numArr[idx + 1]
        else:
            if tot < 0:
                tot = abs(tot) // numArr[idx + 1]*(-1)
            else:
                tot //= numArr[idx + 1]

        # 연산자 사용
        operators[i] -= 1
        backTracking(idx+1, tot)
        operators[i] += 1 # 연산자 복구
        tot = temp # 수 복구

n = int(input())
numArr = list(map(int, input().split()))
operators = list(map(int, input().split()))
minAns = float('Inf') # 양의 무한대
maxAns = float('-Inf') # 음의 무한대

backTracking(0, numArr[0])
print(maxAns)
print(minAns)
