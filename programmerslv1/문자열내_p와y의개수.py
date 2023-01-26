def solution(s):
    a = s.lower()
    p_cnt = a.count('p')
    y_cnt = a.count('y')
    if (p_cnt == 0) and (y_cnt == 0):
        return True
    elif p_cnt == y_cnt:
        return True
    else:
        return False