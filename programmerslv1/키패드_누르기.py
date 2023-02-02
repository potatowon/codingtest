'''
상하좌우 1칸

147 왼
369 오

2580 더 가까운 엄지 -> 만약 거리가 같다면 hand

각번호를 누른 손가락을 연속된 문자열로 return
'''

def solution(numbers, hand):
    answer = ''
    key_pad = {1:[0,3] , 2:[1,3], 3:[2,3], 4:[0,2], 5:[1,2], 6:[2,2], 7:[0,1], 8:[1,1], 9:[2,1], '*':[0,0], 0:[1,0], '#':[2,0]}
    rt = [3, 6, 9, 'star']
    lt = [1, 4, 7, 'jung']
    lt_point = key_pad['*']
    rt_point = key_pad['#']
    for num in numbers:
        if num in lt:
            answer += "L"
            lt_point = key_pad[num]
        elif num in rt:
            answer += "R"
            rt_point = key_pad[num]
        else:
            d_num = key_pad[num]
            if (d_num[0] - lt_point[0])**2 + (d_num[1] - lt_point[1])**2 < (d_num[0] - rt_point[0])**2 + (d_num[1] - rt_point[1])**2:
                answer += "L"
                lt_point = d_num
            elif (d_num[0] - lt_point[0])**2 + (d_num[1] - lt_point[1])**2 > (d_num[0] - rt_point[0])**2 + (d_num[1] - rt_point[1])**2:
                answer += "R"
                rt_point = d_num
            else:
                if hand == 'right':
                    answer += 'R'
                    rt_point = d_num
                else:
                    answer += "L"
                    lt_point = d_num
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")) # "LRLLLRLLRRL"


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
