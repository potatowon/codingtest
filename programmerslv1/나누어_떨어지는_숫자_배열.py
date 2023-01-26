def solution(arr, divisor):
    answer = [n for n in arr if n%divisor == 0]
    answer.sort()
    return [-1] if len(answer) == 0 else answer