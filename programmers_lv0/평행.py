# def solution(dots):
    ''' 평행이라 함은 기울기가 같은것을 의미한다.
    기울기를 구하는것은 y축 증가량/ x축 증가량이다.
    그 값을 하나하나 구해 계산하는건 어렵지 않으나 코드를 간소화 해보자'''
    # tline = [[] for _ in range(len(dots))]
    # for fix_idx in range(len(dots)):
    #     for idx in range(len(dots)):
    #         x_dis = dots[fix_idx][0] - dots[idx][0]
    #         y_dis = dots[fix_idx][1] - dots[idx][1]
    #         if x_dis == 0:
    #             tline[fix_idx].append(0)
    #         else:
    #             tline[fix_idx].append(y_dis/x_dis)
    # t1 = tline[0][1:]
    # t2 = tline[1][2:]
    # t3 = tline[2][3:]
    # result =  t1 + t2 + t2
    # for i in result:
    #     if result.count(i) >= 2:
    #         return 1
    #     else:
    #         return 0
def solution(dots):
    t1 = (dots[1][1] - dots[0][1])/(dots[1][0] - dots[0][0])
    t2 = (dots[2][1] - dots[0][1]) / (dots[2][0] - dots[0][0])
    t3 = (dots[3][1] - dots[0][1]) / (dots[3][0] - dots[0][0])
    t4 = (dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
    t5 = (dots[3][1] - dots[1][1]) / (dots[3][0] - dots[1][0])
    t6 = (dots[3][1] - dots[2][1]) / (dots[3][0] - dots[2][0])
    result = [t1, t2, t3, t4, t5, t6]
    for i in result:
        if result.count(i) >= 2:
            return 1
    return 0
    answer = 0
    return answer

solution([[1, 4], [9, 2], [3, 8], [11, 6]])