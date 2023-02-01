'''
숫자 하나를 주고, m 개의 숫자를 제거하여 가장 큰 수 만들기 단, 순서는 유지
'''

# s, m = map(int, input().split())
s = 9977252641
m = 5

numbers = list(map(int, str(s)))
stack = []

for x in numbers:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)
if m != 0:
    stack = stack[:-m]

res = ''.join(map(str, stack))

print(res)