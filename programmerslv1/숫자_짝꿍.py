'''
두 수에서 공통으로 나타나는 정수를 이용하여 만들 수 있는 가장 큰 정수

존재하지 않으면 -1
'''
# def solution(X, Y):
#     x = list(X)
#     y = list(Y)
#     res = []
#     for s in x:
#         if s in y:
#             res.append(y.pop(y.index(s)))
#     if res:
#         integer = int(''.join(sorted(res, reverse=True)))
#         return str(integer)
#     else:
#         return '-1'
#
# print(solution('5525', '1255'))


def solution(X, Y):
    num = '0123456789'
    answer = ''
    for k in num:
        x = X.count(k)
        y = Y.count(k)
        k_num = k * min(x, y)
        answer += k_num
    if answer:
        if answer == '0' * len(answer):
            return '0'
        # n = int(''.join(sorted(answer, reverse=True)))
        else:
            return ''.join(sorted(answer, reverse=True))
    else:
        return "-1"
print(solution('5525', '1255'))
a = '000'
print(a == len(a))