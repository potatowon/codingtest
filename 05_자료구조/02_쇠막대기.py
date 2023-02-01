'''
쇠막대기를 위로 겹치고 레이저를 위에서 수직으로 발사하여 쇠막대기들을 자른다.

- 자신보다 긴 쇠막대기 위에만 놓일 수 있다. (단, 끝점이 겹치면 안된다)
- 레이저는 적어도 하나
- 레이저는 양끝과 겹치지 않는다.

#
쇠막대기와 레이저의 배치를 나타내는 괄호 표현

잘려진 쇠막대기의 합
'''

import sys

s = sys.stdin.readline().strip()
stack = []
cnt = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == "(":
            # stack.pop()
            cnt += len(stack)
        else:
            # stack.pop()
            cnt += 1

print(cnt)
