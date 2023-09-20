import sys

left_stack = list(input().rstrip())  # 커서의 왼쪽에 있는 문자들
right_stack = []  # 커서의 오른쪽에 있는 문자들
m = int(input())

for _ in range(m):
    cmd = sys.stdin.readline().rstrip()
    
    if cmd[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
            
    elif cmd[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
            
    elif cmd[0] == 'B':
        if left_stack:
            left_stack.pop()
            
    elif cmd[0] == 'P':
        left_stack.append(cmd[2])

# 마지막으로 남아있는 문자들을 결합
print(''.join(left_stack + right_stack[::-1]))
