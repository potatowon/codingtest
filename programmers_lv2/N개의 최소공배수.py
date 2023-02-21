'''
arr에 대한 최소 공배수를 구하시오

arr 15개 이하
'''

def solution(arr):
    arr.sort(reverse=False)
    def gcd(a, b):
        while b != 0:
            a, b = b, a%b
        return a
    def lcm(a, b):
        return (a*b)//gcd(a, b)
    lcm_ = lcm(arr[0], arr[1])
    for i in arr[2:]:
        lcm_ = lcm(lcm_, i)

    return lcm_

solution([2, 6, 8, 14])




