'''
연속된 자연수들로 n을 표현하는 방법의 수를 구하시오

'''


def solution(n):
    prifix_sum = [0]*n
    cnt = 0
    num = [i for i in range(1, n+1)]
    prifix_sum[0] = num[0]
    for i in range(1, n):
        prifix_sum[i] = prifix_sum[i-1] + num[i]
    prifix_sum = [0]+prifix_sum
    for j in range(1, n+1):
        for i in range(j, n+1):
            answer = prifix_sum[i] - prifix_sum[j-1]
            if answer == 15:
                cnt += 1
    return cnt


print(solution(15))