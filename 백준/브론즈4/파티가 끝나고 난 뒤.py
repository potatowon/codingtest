'''
1m^2 당 몇명의 사람

'''

l, p = map(int, input().split(' '))
num = list(map(int, input().split(' ')))

sol = p*l
res = [n-sol for n in num]
print(*res)