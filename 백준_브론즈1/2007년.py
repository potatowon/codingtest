'''
1월 1일은 월요일 x월 y일은 무슨요일일까?
나머지 1 월 2 화 3 수 4 목 5 금 6 토 0 일
[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
[SUN, MON, TUE, WED, THU, FRI, SAT]
'''

x, y = map(int, input().split())

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
dates = sum(months[:x]) + y
print(day[dates%7])