'''

서로다른 n 개의 자연수의 합이 s

n의 최댓값?

'''
s = int(input())
n = 1
while n*(n+1)//2 <= s:
    n += 1
print(n-1)