# 캐릭터의 좌표

'''
이동하는 문제 다만, 보드의 크기를 벗어나게 되면 무시
'''

def solution(keyinput, board):
    answer = [0, 0]
    for key in keyinput:
        if key == 'right' and (answer[0]+1 <= round(board[0]/2)):
            answer[0] += 1
        elif key == 'left' and (answer[0]-1 >= -int(board[0]/2)):
            answer[0] -= 1
        elif key == 'up' and (answer[1]+1 <= round(board[1]/2)):
            answer[1] += 1
        elif key == 'down' and (answer[1]-1 >= -int(board[1]/2)):
            answer[1] -= 1
    return answer

print(solution(	["down", "down", "down", "down", "down"], [7, 9]))
print(solution(["up", "up", "up", "down"],[3, 3]))
