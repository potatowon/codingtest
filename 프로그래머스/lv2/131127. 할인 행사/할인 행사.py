def solution(want, number, discount):
    answer = 0
    w_n = dict()
    for w, n in zip(want, number):
        w_n[w] = n
    for i in range(len(discount)):
        dic = w_n.copy()
        for dc in discount[i:i+10]:
            if dc in dic.keys():
                dic[dc] -= 1
        if all(num <= 0 for num in dic.values()):
            answer += 1
    return answer