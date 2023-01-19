# 격자판 최대의 합

'''
5*5 의 격자판이 주어져있을때, 각 행의 합 열, 두 대각선의 합중 가장 큰 합을 출력하시오...
'''

import sys

N = int(input())
# mat = list()
# for _ in range(N):
#     row_data = list(map(int, sys.stdin.readline().split()))
#     mat.append(row_data)
''' apend 없이 여러행을 리스트화 하기'''
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

largest = -555555

for i in range(N):
    sum1=sum2=0
    for j in range(N):
        sum1 += data[i][j] # 행의 합
        sum2 += data[j][i] # 열의 합
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

sum1=sum2=0
# 대각선의 합

for i in range(N):
    sum1 = data[i][i]
    sum2 = data[i][N-i-1]

if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2

print(largest)