# 문자열 밀기

'''
A 를 몇번 밀어야 B가 될 수 있는지 확인하시오
123456
2번
654123
'''


def solution(A, B):
    cnt = 0
    while cnt != len(A)+1:
        C = A[-cnt:] + A[:-cnt]
        if C == B:
            return cnt
        else:
            cnt += 1
    return -1
print(solution("hello", "ohell"))
print(solution("apple", "elppa"))
print(solution('1234567','5671234'))
k = '1234567'
k = k[-3:] + k[:-3]
print(k)
