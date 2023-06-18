def solution(msg):
    answer = []
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic = {a: idx + 1 for idx, a in enumerate(alpha)}
    num = 27
    w, c = 0, 1

    while w < len(msg):

        while c <= len(msg) and msg[w:c] in dic:
            c += 1
        
        answer.append(dic[msg[w:c-1]])
        

        if c <= len(msg):
            dic[msg[w:c]] = num
            num += 1

        w = c - 1
        
    return answer

