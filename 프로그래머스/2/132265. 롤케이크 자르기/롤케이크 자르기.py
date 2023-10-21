'''
동일한 가짓수의 토핑이 올라가면 된다. 
토핑을 공정하게 자르는 방법의 수를 return
'''
from collections import defaultdict

def solution(topping):
    answer = 0
    b = defaultdict(int)
    for i in topping:
        b[i] += 1
    a = set()
    for i in topping:
        b[i] -= 1
        if b[i] == 0:
            del b[i]
        a.add(i)
        if len(a) == len(b):
            answer +=1
        
    return answer
        
        
