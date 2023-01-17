# 다음에 올 숫자

def solution(common):
    if abs(common[0] - common[1]) == abs(common[1] - common[2]):
        return common[-1] + (common[-1] - common[-2])
    if (common[1] / common[0]) == (common[2] / common[1]):
        return common[-1] * (common[-1] // common[-2])
#