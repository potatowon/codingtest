def solution(n):
    a = n
    res = []
    while a >= 3:
        a, b = a//3, a%3
        res.append(b)
    res.append(a)
    res.reverse()
    sum_ = 0
    for idx, num in enumerate(res):
        sum_ += num*3**idx
    return sum_

print(int('1210', 3))