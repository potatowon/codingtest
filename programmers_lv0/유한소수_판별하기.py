# 유한소수 판별하기

'''
소수로 고칠때 유한소수 인지 판별하시오
-> 기약분수로 나타냈을때 분모에 2, 5만 존재해야한다.
유한소수 이면 1 무한소수 이면 2 return

a, b 의 최대공약수로 두 수를 나눠주고, b의 약수가 2, 5만 존재해야한다.
'''
def solution(a, b):
    divisor = []
    for i in range(1, max(a, b)+1):
        if (a%i == 0) and (b%i == 0):
            lcm = i
    numerator = b//lcm # 분모
    denumerator = a//lcm # 분자
    # 약분했을때 자연수가 되는 경우
    if b == 1:
        return 1
    # 약분해도 분수인 경우
    else:





# test

print(solution(12,21))


