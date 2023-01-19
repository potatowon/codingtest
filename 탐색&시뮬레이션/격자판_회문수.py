''' 5자리의 회문수를 행과 열을 탐색하라!'''

import sys
# 7행 7열의 보드
board = [list(map(int, sys.stdin.readline().split())) for _ in range(7)]
cnt = 0
# 행의 회문 판단.
for i in range(3): # i = 0 일때 0-4, 1-5, 2-6 각 행에 대해 5개의 열씩 3번 판단하면 된다.
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]: # 회문의 판단
            cnt += 1

        for k in range(2):  # 열의 회문 판단
            if board[i+k][j] != board[i+5-k-1][j]:
                break
            else:
                cnt += 1

'''
열의 경우는 리스트가 아니기 때문에 slicing을 할 수 없다 -> 따라서 별도의 for 문을 이용하여 해야한다.
'''
