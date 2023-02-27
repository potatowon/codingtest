from collections import deque


def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    
    while len(cards1) > 0 and len(cards2) > 0 and len(goal) > 0:
        a = cards1.popleft()
        b = cards2.popleft()
        c = goal.popleft()
        
        if a == c or b == c:
            if a == c:
                cards2.appendleft(b)
            else:
                cards1.appendleft(a)
        else:
            return "No"
    if (cards1 == goal) or (cards2 == goal) or (len(goal) == 0):
        return 'Yes'
    else:
        return 'No'
    


'''
def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"    
'''