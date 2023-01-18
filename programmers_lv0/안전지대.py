''' 안전지대 폭탄과 그 상하좌우, 대각선은 모두 반경안에 든다. 그외의 안전지대의 칸수를 구하시오'''





def solution(board):
    new_board = [[-1 for _ in range(len(board)+2)] for _ in range(len(board)+2)]
    safe_board = [[-1 for _ in range(len(board)+2)] for _ in range(len(board)+2)]
    for i in range(1, len(new_board)-1):
        for j in range(1, len(new_board)-1):
            new_board[i][j] = board[i-1][j-1]
    for i in range(1, len(new_board)-1):
        for j in range(1, len(new_board)-1):
            safe_board[i][j] = board[i-1][j-1]


    for i in range(1, len(new_board)-1):
        for j in range(1, len(new_board)-1):
            if safe_board[i][j] == 1:
                new_board[i-1][j-1] += 2
                new_board[i-1][j] += 2
                new_board[i-1][j+1] += 2
                new_board[i][j-1] += 2
                new_board[i][j] += 2
                new_board[i][j+1] += 2
                new_board[i+1][j-1] += 2
                new_board[i+1][j] += 2
                new_board[i+1][j+1] += 2
    print(safe_board)
    print(new_board)
    cnt = 0
    for k in range(1, len(new_board)-1):
        cnt += new_board[k].count(0)


    return cnt

solution( [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]])