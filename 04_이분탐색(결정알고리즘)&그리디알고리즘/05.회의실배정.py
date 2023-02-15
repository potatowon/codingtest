'''
n 개의 회의들에 대해아ㅕ 회의실 사용표를 만들려고 한다.
시작시간 : 끝나는 시간
겹치지 않게 회의실을 사용할 수 있는 최대수의 회의를 찾아라
'''

# 아이디어 : 끝나는 시간을 기준으로 정렬하라
# 빨리끝나는것이 중요함.. 그래야 회의 갯수를 많이 할 수 있다

import sys

n=int(input())
meeting=[]
for i in range(n):
    a, b=map(int, input().split())
    meeting.append((a, b))
meeting.sort(key=lambda x : (x[1], x[0])) ## 정렬 순위는 튜플로 정해주면 된다.
et=0
cnt=0
for x, y in meeting:
    if x>=et:
        et=y
        cnt+=1
print(cnt)