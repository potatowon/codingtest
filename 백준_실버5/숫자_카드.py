n = int(input())
cards = set(map(int, input().split()))
m = int(input())
judge = map(int, input().split())

for num in judge:
    if num in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')


'''
map 함수가 반환하는 객제가 iterator 이기 때문이다. iterator는 한번만 순회가 가능하고 순회 후에는 빈 상태가 된다. 

iterator 에 대해 알아보기

set의 in 연산의 경우는 O(1) 이므로 list 보다 빠르다. 

https://twpower.github.io/120-python-in-operator-time-complexity : 시간복잡도
'''