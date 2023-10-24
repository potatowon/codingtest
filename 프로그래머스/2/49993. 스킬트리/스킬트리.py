def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        res = ''
        for t in tree:
            if t in skill:
                res += t
        if res == skill[:len(res)]:
            answer += 1
    return answer