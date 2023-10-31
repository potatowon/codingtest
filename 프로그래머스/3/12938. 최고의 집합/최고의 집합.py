def solution(n, s):
    if n > s:
        return [-1]  # n이 s보다 큰 경우 최고의 집합이 존재하지 않음

    quotient = s // n
    remainder = s % n

    result = [quotient] * (n - remainder) + [quotient + 1] * remainder

    return result
