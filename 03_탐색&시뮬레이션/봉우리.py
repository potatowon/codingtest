'''
N*N 격자판이 주어진다. 지역의 높이가 쓰여있다. 상하좌우보다 크면 봉우리다. 봉우리 지역이 몇개 있는지 구하시오
격자 가장자리는 0으로 초기화 되었다고 가정한다.
'''
''' 다 맞음'''
import sys

N = int(input())
data = []
for _ in range(N):
    d = list(map(int, sys.stdin.readline().split()))
    data.append(d)

board = [[0 for _ in range(N+2)] for _ in range(N+2)]

for i in range(1, N+1):
    for j in range(1, N+1):
        board[i][j] = data[i-1][j-1]

'''
pad 만드는 방법

a.insert(0, [0]*n) 0 행에 0만가진 행렬 추가
a.append([0]*n) #마지막 행에 0만 가진 행렬 추가
for x in a:
    a.insert(0, 0) # 0번인덱스에 0 넣기 
    a.append(0) # 끝자리에 0 넣기
'''

# 만약 봉우리면 인덱스를 2칸 증가하고, 아니면 1칸 증가... (옆으로는)
## 위아래로는 ? 마찬가지 근데 이걸 어떻게 구현하는가가 문제....
cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(1, N+1):
    for j in range(1, N+1):
        if all(board[i][j] > board[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
print(cnt)