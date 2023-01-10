# 직사각형 넓이 구하기

'''
4개의 꼭직점 좌표가 주어지고 각 직사각형의 넓이를 구하시오
'''
#
# def solution(dots):
#     import numpy as np
#     dots = np.array(dots)
#     x_distance = max(dots[: ,0]) - min(dots[:,0])
#     y_distance = max(dots[:,1]) - min(dots[:,1])
#     return x_distance*y_distance



def solution(dots):
    x_dots = []
    y_dots = []
    for data in dots:
        x_dots.append(data[0])
        y_dots.append(data[1])
    x_dis = max(x_dots) - min(x_dots)
    y_dis = max(y_dots) - min(y_dots)
    return x_dis*y_dis



print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))
dots = [[1, 1], [2, 1], [2, 2], [1, 2]]
print(max(dots)) # max 하면 각 행 비교해서 max 값 도출

# def solution(data):

