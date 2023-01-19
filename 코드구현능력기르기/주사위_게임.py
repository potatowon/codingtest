'''
같은 눈이 3개 -> 10,000 * (눈 * 1,000)
같은 눈 2개  -> 1,000 * (눈 * 100)
모두 다른 눈 -> 가장 큰눈 * 100
'''
import sys
n = int(sys.stdin.readline())
total_money = []
for i in range(n):
    tmp = sys.stdin.readline().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if (a==b) and (b==c):
        money = 10000+a*1000
    elif (a==b) or (a==c): # elif는 if 가 참일 경우 돌아가지 않기 때문에 논리식에 3가지 경우가 같은 게 모두 포함 된다 하더라도 위에서 걸러진다.
        money = 1000+(a*100)
    elif b==c:
        money = 1000 +(b*100)
    else:
        money = c*100
    total_money.append(money)
print(max(total_money))
