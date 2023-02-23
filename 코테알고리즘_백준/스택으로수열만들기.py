'''
실버3 1874

1 부터 n 스택에 저장하고 출력하는 방식으로 하나의 수열을 만들 수 있다.
push 하는 순서는 반드시 오름차순을 지키도록 한다.

수열을 만들기 위한 연산 push + , pop -, 불가하면 no 출력

'''
import sys
ans = ''
stack = []
n = int(input())
i = 1 # while 문 용 초기화
# n 번 만큼 돌림 for 문
for _ in range(n):
    # 원하는 값을 일단 받고
    val = int(sys.stdin.readline())
    if i <= val:
        while True:
            stack.append(i)
            ans += '+\n'
            i += 1
            if stack and (stack[-1] == val):
                ans += '-\n'
                stack.pop()
                break
    
    else:
        # n = stack.pop()
        if val < stack[-1]:
            ans = "NO"
            break
        else:
            ans += '-\n'
            stack.pop()
            

print(ans)

# 1. push 
# 2. pop