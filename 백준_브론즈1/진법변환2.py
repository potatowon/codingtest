n, b = map(int, input().split())

answer = []
while n:
    remainder = n % b
    if remainder > 9 :
        answer.append(chr((ord('A') + (remainder - 10)))) # 10 진수 이상인경우 영어로 표현
    else:
        answer.append(str(remainder))
    n //= b

print(''.join(answer[::-1]))