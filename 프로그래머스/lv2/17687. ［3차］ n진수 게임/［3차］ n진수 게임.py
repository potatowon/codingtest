import string

tmp = string.digits+string.ascii_uppercase
# print(tmp)
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]
def solution(n, t, m, p):
    lst = ''
    for i in range(t*m):
        lst += convert(i, n)
    # print(lst)
    # print(len(lst))
    answer = ''
    order = p
    while len(answer) < t:
        answer += lst[order-1]
        order += m
    return answer