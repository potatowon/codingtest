'''
k 과자한개의 가격
n 사려고 하는 과자
m 현재 소지 금액


'''

k, n, m = map(int, input().split(' '))
print(k*n-m if k*n > m else 0)
