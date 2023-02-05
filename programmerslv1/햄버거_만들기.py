'''
재료 조리 시 -> 아래서 부터 위로 stack

쌓아서 햄버거 완성
(빵, 야채, 고기 , 빵)

[야채, 빵, 빵, 야채, 고기, 빵, 야채, 고기, 빵]

1: 빵
2: 야채
3: 고기
-> 1231
'''
from collections import deque
def solution(ingredient):
    ingredient = deque(ingredient)
    stack = []
    answer = 0
    while ingredient:
        i = ingredient.popleft()
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                stack.pop()

    return answer


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))