'''
진도가 100% 일 때 서비스에 반영할 수 있다.

기능의 개발 속도가 다 달라 뒤에 기능이 앞에 기능보다 먼저 개발 이 경우 -> 뒤에 있는 기능은 앞에 기능이 배포 될때 함께 배포
먼저 배포되어야 하는 순서/작업의 개발 속도

배포는 하루에 한번

각 배포일에 배포되는 수를 return
'''
from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses:
            now = progresses.popleft()
            now_speed = speeds.popleft()
            if now >= 100:
                cnt += 1
            else:
                progresses.appendleft(now)
                speeds.appendleft(now_speed)
                break
        if cnt > 0:
            answer.append(cnt)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([1,1,1,1], [100, 50, 99, 100]))