'''
기사 번호 개수의 약수 개수에 해당하는 공격력을 가진 무기 구매
단, 공격력 제한수치 -> 큰 무기 구매 협약기관 정한 공격력

공격력 1당 1kg
필요한 철의 무게 계산
'''

def solution(number, limit, power):
    divisor_num = []
    for j in range(1, number+1):
        cnt = 0
        for i in range(1, int(j**0.5) +1 ):
            if (j == i**2):
                cnt +=1
            elif (j%i == 0):
                cnt +=2
        divisor_num.append(cnt)
    print(divisor_num)
    res = [i if i <= limit else power for i in divisor_num ]
    return sum(res)

print(solution(5, 3, 2))

