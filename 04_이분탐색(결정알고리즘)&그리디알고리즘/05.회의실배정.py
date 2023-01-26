'''
n 개의 회의들에 대해아ㅕ 회의실 사용표를 만들려고 한다.
시작시간 : 끝나는 시간
겹치지 않게 회의실을 사용할 수 있는 최대수의 회의를 찾아라


'''

import sys

n = int(input())

tl = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # time list
tl.sort(key=lambda x: abs(x[0]-x[1]))
# tl.sort(key=lambda x: x[0])

print(tl)