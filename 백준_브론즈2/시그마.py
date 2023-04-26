'''
두 정수 사이의 수의 합
'''

A, B = map(int, input().split())
a = max(A, B)
b = min(A, B)

s_n = (a*(a+1))//2
s_i = (b*(b-1))//2

print(s_n - s_i)