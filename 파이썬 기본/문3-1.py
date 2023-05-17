'''
같은 이름을 찾아 집합으로 만들어 retrun
'''

def solution(names):
    sames = set()
    n_names = len(names)
    for i in range(n_names):
        for j in range(i+1, n_names):
            if names[i] == names[j]:
                sames.add(names[j])
                break

    return sames

print(solution(['Tom', 'jack', 'Mikle', 'Tom']))