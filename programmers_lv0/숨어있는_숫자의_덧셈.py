# Lv0
'''
my_string 안의 자연수들의 합을 return
edge case : 자연수가 없는경우 0을 Return
'''
def solution(my_string):
    word_s = 'abcdefghijklmnopqrstuvwxyz'
    word_b = word_s.upper()
    word = word_s + word_b
    if my_string.isalpha():
        return 0
    else:
        for i in word:
            my_string = my_string.replace(i, '+')
        my_string = list(my_string)
        while my_string[-1] == '+':
            my_string.pop()
        result = ''.join(my_string)
        return eval(result)