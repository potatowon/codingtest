'''
(), [], {}
올바른 문자열

'''
from collections import deque
def solution(s):
    s = deque(s)
    cnt = 0
    for _ in range(len(s)):
        s.rotate(1)
        # print(s)
        words = ''.join(s)
        for _ in range(len(s)):
            words = words.replace('()','').replace('[]','').replace('{}','')
        if words == '':
            cnt +=1
    return cnt

# from collections import deque
#
# a = deque([1,2,3,4,5])
# for _ in range(5):
#     a.rotate(1)
#     print(a)

# a = '([]){}'
# for _ in range(2):
#     a = a.replace('()','').replace('[]','').replace('{}','')
# print(a)

# print(solution("[](){}"))
# print(solution("[)(]"))
print(solution("[{]}()"))
print(solution("{{{}"))
