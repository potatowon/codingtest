def solution(lines):
    A = [i for i in range(max(lines[0][0], lines[1][0]),min(lines[0][1], lines[1][1]))]
    B = [i for i in range(max(lines[0][0], lines[2][0]),min(lines[0][1], lines[2][1]))]
    C = [i for i in range(max(lines[1][0], lines[2][0]),min(lines[1][1], lines[2][1]))]
    A = set(A)
    B = set(B)
    C = set(C)
    result = (A | B | C)
    print(result)
    if len(result) == 0:
        answer = 0
    if len(result) >= 1:
        answer = len(result)
    return answer