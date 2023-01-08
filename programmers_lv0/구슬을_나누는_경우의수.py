# 구슬을 나누는 경우의 수

'''
머쓱이가 갖고 있는 구슬 balls , 나누어줄 구슬의 개수 share
balls 중 share의 구슬을 고르는 경우의 수

5개 가지고 있고 3개 나눠 줄거다  -> 5C3 combination
nCr  = n! / (n-r)!*r!
'''

def solution(balls, share):
    import math
    answer = (math.factorial(balls)/(math.factorial(share)*math.factorial(balls-share)))
    return int(answer)

# test

print(solution(3,2))
print(solution(5,3))

# factorial 구현
k = 1
for i in range(1,3+1):
    k *= i
print(k)