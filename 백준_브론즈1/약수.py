'''
어떤 수 N 의 진짜 약수가 모두 주어질때 , N 을 구하는 프로그램
'''

n = int(input())
divisor = list(map(int, input().split()))

divisor.sort()
print(divisor[0]*divisor[-1])