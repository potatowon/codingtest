'''
바로 앞 또는 뒤로만 빌려줄 수 있다.

최대한 많은 학생이 체육 수업을 들어야한다.

2 <=n = 전체 학생의 수 <= 30
lost = 도난 당한 학생의 배열
1 <= reserve = 여벌의 체육복을 가져온 학생 <= n

Return : 체육을 들을 수 있는 학생 수의 최대값.
'''
a = [4,5,6,7,8,9]
def solution(n, lost, reserve):
    answer = 0
    students = [False] + [True]*n
    for i in lost:
        if i in reserve:
            reserve.remove(i)
        else:
            students[i] = False
    reserve.sort()
    for j in reserve:
        if j == 1:
            students[j+1] = True
        elif j == n:
            students[n-1] = True
        else:
            if not students[j-1]:
                students[j-1] = True
            elif not students[j+1]:
                students[j+1] = True

    for k in students:
        if k:
            answer += 1
    # print(students)
    # print(reserve)
    return answer

print(solution(5, [2, 4], [1,3,5])) # 5
print(solution(7, [2,4,7], [1,4,5]))# 6
print(solution(5, [5], [4])) # 5
print(solution(13, [1, 2, 5, 6, 10, 12, 13], [2,3,4,5,7,8,9,10,11,12])) # 11
# 24 20 18 10 9 1 2 3 5 6 7