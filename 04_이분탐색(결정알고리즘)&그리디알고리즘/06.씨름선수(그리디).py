'''
N명의 지원자가 지원 - 키와 몸무게
키와 몸무게 중 적어도 하나는 크커나, 무거운 지원자 만 뽑기로한다.
'''
import sys

n = int(input())

appliers = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

appliers.sort(key=lambda x: x[0])
# print(appliers)
cnt = 0
for idx in range(len(appliers)-1):
    applier = appliers[idx]
    non_pass = True
    for c in appliers[idx+1:]:
        if applier[1] <= c[1]:
            non_pass = False
    if non_pass:
        cnt += 1
cnt += 1

print(cnt)