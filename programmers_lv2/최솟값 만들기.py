'''
길이가 같은 배열 A,B 각 배열은 자연수로 이루어져 있음.

A, B에서 각각 한개를 뽑아 두 수를 곱한다. 배열의 길이만큼 반복하여 누접 합

누적 합이 최소가 되도록

배열의 길이 1000
'''

def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for a, b in zip(A, B):
        answer += a*b
    return answer


print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))