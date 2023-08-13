def solution(word):
    chars = 'AEIOU'
    weight = [781, 156, 31, 6, 1]  # 5^4 + 5^3 + 5^2 + 5 + 1 -> 5의 합의 공식

    answer = 0
    for i in range(len(word)):
        answer += weight[i] * chars.index(word[i]) + 1

    return answer
