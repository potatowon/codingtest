import sys

n = int(input())
colorPaper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
white = 0
blue = 0
def divideAndConquer(x, y, n): # (x, y) 의 시작점 n = 종이의 길이
    global white, blue # count 변수 초기화
    colorStandard = colorPaper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if colorPaper[i][j] != colorStandard:
                divideAndConquer(x, y, n//2)
                divideAndConquer(x+n//2, y, n//2)
                divideAndConquer(x, y+n//2, n//2)
                divideAndConquer(x+n//2, y+n//2, n//2)
                return
    if colorStandard == 1:
        blue +=1
        return
    else:
        white +=1
        return

divideAndConquer(0, 0, n)
print(white)
print(blue)