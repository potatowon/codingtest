''' 숫자열을 뒤집은 리스트로 출력하시오 '''

def digit_reverse(n):
    return list(map(int, reversed(str(n))))