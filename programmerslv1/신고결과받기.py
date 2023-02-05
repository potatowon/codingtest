'''
게시판 불량 이용자 신고하고 처리 결과 메일로 발송

한 번에 한 유저 신고
동일 유저 신고는 1회 처리

k 번이상 신고된 유저는 이용 정지, 해당 유저를 신고한 모든 유저에게 사실 발송

id_list : 이용자의 id
report : 각 이용자가 신고한 이용자의 id 정보
k : 정지 당하기 위한 신고 횟수

결과 각 id_list 순으로 결과 메일을 받은 횟수
'''

def solution(id_list, report, k):
    report_cnt = {}
    report_id = {}
    stoped_id = []
    answer = [0]*len(id_list)
    for i in id_list:
        report_cnt[i] = 0
        report_id[i] = []
    report = list(set(report))
    for j in report:
        n, m = j.split(' ')
        report_cnt[m] += 1
        report_id[n].append(m)
    for s, v in report_cnt.items():
        if v >= k :
            stoped_id.append(s)
    for idx, user in enumerate(id_list):
        user_report = report_id[user]
        for i in stoped_id:
            if i in user_report:
                answer[idx] += 1
    return answer





print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))