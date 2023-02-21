'''
알파벳 소문자로 이루어진 문자열 -> 같은 문자열 2개가 있으면 제거한다.

모두 제거 할 수 있다면 1, 아니면 0을 return
'''
from collections import deque

def solution(s):
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return 1 if stack == [] else 0

print(solution('baabaa'))
print(solution('cdcd'))