'''
길이 l 의 창고가 있고
각 열에는 높이들이 달리 짐이 쌓여있다
가장 높은 곳에서 가장 낮은 곳으로 짐을 옮기는 것을 m 회 반복하여
가장 높은 곳과 낮은 곳의 차이를 구하시오
'''

import sys

l = int(input())
box = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

for _ in range(m):
    box[box.index(max(box))], box[box.index(min(box))] = max(box)-1, min(box)+1
print(max(box) - min(box))
