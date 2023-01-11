
#
def solution(polynomial):
    poly = polynomial.split(' + ')
    result = [0 ,0]
    for term in poly:
        if 'x' in term:
            if term == 'x':
                term = '1x'
            x_term = term.replace('x','')
            result[0] += int(x_term)
        else :
            result[1] += int(term)
    if result[0] == 0:
        return f'{result[1]}'
    if result[1] == 0:
        if result[0] == 1:
            return f'x'
        else:
            return f'{result[0]}x'
    else:
        if result[0]==1:
            return f'x + {result[1]}'
        else:
            return f'{result[0]}x + {result[1]}'
#
#
#
print(solution("3x + 7 + x"))
# print(eval('3x + 7 + x'))
