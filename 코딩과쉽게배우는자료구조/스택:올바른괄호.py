from collections import deque

def solution(s):
    stack = deque()
    s = deque(s)
    while s:
        
        tmp = s.popleft()
        
        if not stack:
            stack.append(tmp)
        elif stack[0] == ')':
            return False
        elif stack[-1] == '(' and tmp == ')':
            stack.popleft()
        else:
            stack.append(tmp)
    if stack:
        return False

    return True
            
            