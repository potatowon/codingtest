def solution(s):
    result = []
    answer = []
    #     for pt in range(len(s):

    for idx in range(len(s)):
        if s[idx] in answer:
            target = s[idx]
            for j in range(idx):
                if s[j] == target:
                    res = j
            result.append(abs(res - idx))
        else:
            result.append(-1)
            answer.append(s[idx])
    return result