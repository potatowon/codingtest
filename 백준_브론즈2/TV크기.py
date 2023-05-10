'''
TV의 대각선 길이, 높이와 너비의 비율이 주어졌을때 실제 높이와 너비의 길이를 출력하는 프로그램
h:w = ax:bx
l^2 = 4x^2 + 9x*2
l^2 = 13x^2

x = (l^2/a^2+b^2)**0.5
'''

D, H, W = map(int, input().split())

x = ((D**2)/(H**2 + W**2))**0.5
h = H*x
w = W*x

print(int(h), end=' ')
print(int(w))