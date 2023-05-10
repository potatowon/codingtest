'''
문자열 s,p 가 주어졌을 때 , p 가 s 의 부분 문자열인가?
'''


s = input().strip()
p = input().strip()

if p in s:
    print(1)
else:
    print(0)