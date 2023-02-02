def solution(board, moves):
    answer = 0
    stack = []
    for idx in moves:
        for jdx in range(len(board)):
            doll = 0
            if board[jdx][idx-1] != 0:
                doll = board[jdx][idx-1]
                board[jdx][idx-1] = 0
                break
        if (doll != 0) and stack:
            if stack[-1] == doll:
                stack.pop()
                answer += 2
            else:
                stack.append(doll)
        elif (doll != 0) and not stack:
            stack.append(doll)

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))