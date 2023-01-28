'''
문자와 숫자가 주어진것을 숫자만 return 하도록 하시오.
'''


def solution(s):
    a = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(a)):
        s = s.replace(a[i], str(i))
    return int(s)