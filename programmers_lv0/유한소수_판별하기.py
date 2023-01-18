# 유한소수 판별하기

'''
소수로 고칠때 유한소수 인지 판별하시오
-> 기약분수로 나타냈을때 분모에 2, 5만 존재해야한다.
유한소수 이면 1 무한소수 이면 2 return

a, b 의 최대공약수로 두 수를 나눠주고, b의 약수가 2, 5만 존재해야한다.
'''
def solution(a, b): # a/b
    # a, b의 최대 공약수
    for i in range(1, min(a, b)+1):
        if (a%i == 0) and (b%i==0):
            lcm = i

    numerate = b//lcm

    # 약분 후 정수 인경우
    if numerate == 1:
        return 1
    # 소인수 분해 해서 소수가 2, 5 만있을 경우
    prime = [False, False] + [True]*(numerate-1)
    for i in range(2, int(numerate**0.5)+1):
        if prime[i]:
            for j in range(i*2, numerate+1, i):
                prime[j] = False
    primes = [i for i in range(0, numerate+1) if prime[i]]

    division = []
    for i in primes:
        if numerate%i == 0:
            division.append(i)

    if (division == [2]) or (division == [5]) or (division == [2, 5]):
        return 1
    else:
        return 2

print(solution(7, 20))




