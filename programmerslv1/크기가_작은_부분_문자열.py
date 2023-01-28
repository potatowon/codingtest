'''
숫자로 이뤄진 문자열 t, p
t에서 p와 길이가 같은 부분 문자열 중, 부분문자열이 나타내는 수 p보다 작거나 같은것이 나오는 횟수를 return
'''

def solution(t, p):
    cnt = 0
    for i in range(0, len(t)-len(p)+1):
        w = t[i:i+len(p)]
        if int(p) >= int(w):
            cnt +=1
    return cnt

print(solution("500220839878", '7'))