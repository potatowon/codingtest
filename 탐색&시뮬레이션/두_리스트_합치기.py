''' 오름 차순 정렬된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력'''

import sys

N = int(input())
lst1 = list(map(int, sys.stdin.readline().split()))
M = int(input())
lst2 = list(map(int, sys.stdin.readline().split()))

result =lst1 + lst2 # 시간복잡도가 nlogn
result.sort()

print(*result)




'''
# sort 의 시간복잡도는 nlog(n) 이다
# 이미 정렬되어있는 경우는 n 이다
따라서 오름차순을 유지하면서 합치는 것이 좋다. -> 합치는 방법 (병합정렬!)

--> 이전에 남아있는 배열을 넣어주는 과정에서 어려움을 겪었다... 그 것을 해결해 보자.

'''

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
m = int(input())
b = list(map(int, sys.stdin.readline().split()))

p1 = p2 = 0 # pointer 변수의 초기화
c = []
while p1 < n and p2 < m: # 둘 중 하나의 포인터라도 끝까지 가면 멈추는 시스템
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

# 누가 남았는지 확인하는 작업
if p1 < n :
    c = c + a[p1:]
if p2 < m :
    c = c + b[p2:]

for x in c:
    print(x, end=' ')