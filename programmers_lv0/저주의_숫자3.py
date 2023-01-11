# 저주의 숫자3

''' 3의 배수와 3을 사용하지 않는다
정수 n 이 주어졌을때, 마을에서 사용하는 숫자로 변경하시오'''

'''
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,...]
[1,2,4,5,7,8,10,11,14,16,17,19,20,...]

마을에서 사용하는 숫자의 목록을 만들어 인덱스로 찾아가자
'''

def solution(n):
    numbers = []
    for num in range(1,300):
        if not((num%3 == 0) or ('3' in str(num))):
            numbers.append(num)
    print(numbers)
    return numbers[n-1]

solution(15)