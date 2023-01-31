'''
스타상  -> 2배
아차상 -> -1배

'''


def solution(dartResult):
    dartResult = dartResult.replace("10", "A")
    stack = []
    bonus = {'S': 1, 'D': 2, 'T':3}
    for s in dartResult:
        if s.isdigit() or s == "A":
            stack.append(10 if s == "A" else int(s))
        elif s in ("S","D", "T"):
            num = stack.pop()
            stack.append(num**bonus[s])
        elif s == '#':
            stack[-1] *= -1
        elif s == '*':
            num = stack.pop()
            if len(stack):
                stack[-1] *= 2
            stack.append(2*num)
    return sum(stack)


print(solution("1S2D*3T"))  # 37
print(solution("1D2S#10S"))
