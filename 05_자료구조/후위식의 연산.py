'''
후위 표기식에서 원래 식으로 만들어 계산해 내는 방식

'''

import sys

expression = sys.stdin.readline().strip() # 후위 연산식 입력받기
stack = []

# 후위 연산식을 순회하며, 스택에 피연산자를 저장하고 연산자를 처리한다.
for ch in expression:
    if ch.isdigit():
        stack.append(int(ch))

    else:
        a = stack.pop()
        b = stack.pop()
        if ch == '+':
            stack.append(a + b)
        elif ch == '-':
            stack.append(a - b)
        elif ch == '*':
            stack.append(a * b)
        elif ch == '/':
            stack.append(a / b)

print(stack[0])