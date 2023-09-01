def solution(name, yearning, photo):
    # name과 yearning을 딕셔너리로 만들어서 O(1)의 시간 복잡도로 접근 가능하게 합니다.
    yearning_dict = {n: y for n, y in zip(name, yearning)}
    
    result = []
    for p in photo: 
        score = 0
        for person in p: 
            score += yearning_dict.get(person, 0)  
        result.append(score)
    return result

