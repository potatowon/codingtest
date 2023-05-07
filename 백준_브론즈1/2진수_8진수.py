# from collections import deque
#
#
# n = input()
# answer = deque()
# ten_num = int(n, 2)
# a, b = ten_num//8, ten_num%8
# answer.appendleft(b)
# while True:
#     if a < 8:
#         break
#     else:
#         a, b = a//8, a%8
#         answer.appendleft(b)
# answer.appendleft(a)
# res = ""
# for i in answer:
#     res += str(i)
#
# print(res)
'''

2진수와 8진수의 관계를 생각해보자
'''

n = input()

# 입력된 2진수가 3자리로 나누어 떨어지지 않을 경우 앞에 0을 추가하여 3자리 단위로 맞춤
while len(n) % 3 != 0:
    n = '0' + n

# 3자리씩 끊어 8진수로 변환
octal_num = ""
for i in range(0, len(n), 3):
    binary_chunk = n[i:i+3]
    octal_digit = int(binary_chunk, 2)
    octal_num += str(octal_digit)

print(octal_num)
