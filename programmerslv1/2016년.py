'''
1월 1일 금요일 -> a월 b일은 무슨 요일

1.1  -> 1일
1.8 -> 8
1.31 -> 31

2.3 -> 31 + 3
3. 15 -> 31 + 29 + 15


'''
def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    dates = -1
    # if a > 1:
    for i in month[:a-1]:
        dates += i
    dates += b
    return day[dates%7]
    # else:
    #     dates += b
    #     return day[dates%7]
print(solution(5, 24))
# month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# print(month[:0])
