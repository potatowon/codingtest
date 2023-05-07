'''
앞으로 읽거나 뒤로 읽어도 같은수
radar sees

무의미한 0은 앞에 올 수 없음
'''

while True:
    num = int(input())

    if num == 0:
        break
    else:
        if str(num) == str(num)[::-1]:
            print('yes')
        else:
            print('no')