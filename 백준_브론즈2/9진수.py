'''
10진수를 9진수로 바꾸자

100 = 11 1

'''

t = int(input())
a, b = t//9, t%9

answer = str(b)
while a > 8 :
    a, b = a//9, a%9
    answer += str(b)
answer += str(a)
# print(answer)
answer = list(answer)
answer.reverse()
# print(answer)
print(str(int(''.join(answer))))