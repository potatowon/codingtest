import numpy
import numpy as np


def solution(N, stages):
    # 실패율 = 도달 but 클리어 x/ 도달
    # n : 전체 스테이지의 개수 , stages : 멈춰있는 스테이지의 번호
        # 실패율이 높은 스테이지 부터 내림차순
    cnt_s = [0 for _ in range(N+2)]
    clear_cnt = [0 for _ in range(N+2)]
    fail_cnt = [0]*(N+2)
    fail = []
    for s in stages:
        for j in range(1, s+1):
            cnt_s[j] += 1 # 도달한 사람수
        for j in range(1, s):
            clear_cnt[j] += 1 # 도달 후 성공
    print(cnt_s)
    print(clear_cnt)
    for i in range(len(clear_cnt)):
        fail_cnt[i] = cnt_s[i] - clear_cnt[i]
    print(fail_cnt)
    for idx in range(len(cnt_s)):
        try:
            fail.append(fail_cnt[idx]/cnt_s[idx])
        except:
            fail.append(0)
    fail_rate = fail[1:-1]
    s = sorted(range(len(fail_rate)), key=lambda x: fail_rate[x] , reverse=True)
    answer = [i+1 for i in s]
    print(answer)
    # dic = {}
    # for k in range(len(fail)):
    #     dic[k] = fail[k]
    # print(dic)
    # 실패율이 낮은거 대로 내림차순
print(solution(5, [2,1,2,6,2,4,3,3])) # 34215
