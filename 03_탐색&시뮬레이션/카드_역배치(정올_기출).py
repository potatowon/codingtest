'''
10개에 줄에 10번에 입력이 주어진다
a~b 까지 현재의 역순으로 바꾼다.
'''
import sys
num = [i for i in range(1, 21)]
for _ in range(10):
    a, b = map(int, sys.stdin.readline().split())
    num[a-1:b] = reversed(num[a-1:b])
print(*num)

#
# a = [i for i in range(11)]
# print(a)
# a[1:3] = reversed(a[1:3])
# print(a)

'''
swap

a = 5
b = 10

a, b = b, a # 아래로 차래로 쓰는경우와는 다른 값이 나오니 주의 바람
 
구간이 2 ~ 7 이면 (2,7) (3,6) (4,6) 뒤집어주는 과정 필요
따라서 7-2+1//2 횟수만큼 돈다
s, e = map(int, sys.stdin.readline().split())
for i in range((e-s+1)//2)):
    s[s+i], a[e-i] = a[e-i], s[s+i]
'''