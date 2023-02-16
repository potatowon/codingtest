''' 스도쿠 검사 '''

'''
각 3*3 배열에 1~9가 중복이 없어야 하고, 각 행에도 중복이 없어야 한다. 
'''
''' 다맞음 '''
import sys

sudoku = []

for _ in range(9):
    s = list(map(int, sys.stdin.readline().split()))
    sudoku.append(s)

# 3*3 배열 확인하기
answer = []
for idx in range(3):
    window = [row[3*idx:3*idx+3] for row in sudoku[3*idx:3*idx+3]]
    result = sum(window, [])
    # print(result)
    for i in range(1, 10):
        if result.count(i) != 1:
            answer.append('NO')
        else:
            answer.append("YES")

# 행에 대해서 따지자

for idx in range(len(sudoku)):
    if sudoku[idx].count(idx+1) != 1:
        answer.append("NO")
    else:
        answer.append("YES")

if all(answer[i] == "YES" for i in range(len(answer))):
    print("YES")
else:
    print("NO")


'''
ch = [0]*10
행, 열, 그룹 별 체크리트를 형성해 그 값들을 Index로 넣는다
즉 
ch[sudoku[i][j]] = 1
sodoku[i][j]  = [1, 4, 3, 2, 4, 5, 8, 1, 7]
각 요소들이 ch 의 인덱스로 작동해 그 인덱스 값에 1을 부여한다.
따라서 모든 요소가 다 있으면
sum(ch) == 9 
임을 이용한다.
'''