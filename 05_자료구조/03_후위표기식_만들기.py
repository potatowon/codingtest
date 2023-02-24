## 풀이식 ##



a = input()
stack=[]
res = ''
for x in a:                             # 입력된 문자열을 앞에서 부터 순서대로 가져온다 '3+5*2/(7-2)
    if x.isdecimal():                   # 숫자면 res +=한다.
        res += x
    ## 숫자가 아닌경우 경우의 수 구하기
    else:
        if x == '(':                
            stack.append(x)
        elif x == '*' or x == '/':          # 곱하기의 경우 바로 앞에 다른 곱하기나 나누기가 있지 않으면 그냥 어펜드 부터 한다.
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(': # 항상 괄호는 먼저 계산 해야 하므로, "(" 가 나오기 전까지의 연산은 모두 한다.
                res += stack.pop()
            stack.pop()                       # 위 연산으로 인해 이 과정에서는 ")" 가 Pop 이 된다.
while stack:        # 과정이 모두 끝났음에도 stack 에 남아있는 것이 있으면 뒤에 마저 붙여주면 된다.
    res += stack.pop()
print(res)
