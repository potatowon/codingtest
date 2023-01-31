def solution(lottos, win_nums):
    p = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    cnt = 0
    for i in lottos:
        if win_nums.count(i):
            cnt += 1
    low = cnt
    high = cnt + lottos.count(0)
    print(p[low])
    print(p[high])
    answer = [p[high], p[low]]
    return answer



print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))