'''
1~n번 까지의 개인정보
약관마다 보관의 유효기간

모든 달은 28일까지 있다고 가정한다.

today 2022.01.01 오늘 날짜
terms '약관종류 유효기간' list
privacies '가입시기 약관의 종류'
'''

def solution(today, terms, privacies):
    answer = []
    ty, tm, td = map(int, today.split('.'))
    tod = [ty, tm, td]
    terms_dic = {}
    for term in terms:
        category, period = term.split(' ')
        terms_dic[category] = int(period)
    # print(terms_dic)
    privacy_dic = {}
    for i, privacy in enumerate(privacies):
        dates, p_category = privacy.split(' ')
        dy, dm, dd = map(int, dates.split('.'))
        privacy_dic[i+1] = [dy, dm, dd, p_category]
    # print(privacy_dic)
    # 만료 기간 계산하기
    period_day = []
    for j in privacy_dic.keys():
        year = privacy_dic[j][0] + ((terms_dic[privacy_dic[j][3]]) // 12)
        month = (privacy_dic[j][1] + (terms_dic[privacy_dic[j][3]]) % 12)
        if month > 12:
            year += 1
            month -= 12
            day = privacy_dic[j][2] - 1
            if day == 0 :
                month -= 1
                day = 28
                if month == 0:
                    year -= 1
                    month = 12
                    day = 28
            period_day.append([year, month, day])
        else:
            # year = privacy_dic[j][0]
            # month = privacy_dic[j][1] + terms_dic[privacy_dic[j][3]]
            day = privacy_dic[j][2] - 1
            if day == 0:
                month -= 1
                day = 28
                if month == 0:
                    year -= 1
                    month = 12
                    day = 28
            period_day.append([year, month, day])
    print(period_day)
    print(tod)
    for idx, date in enumerate(period_day):
        if tod[0] > date[0]:
            answer.append(idx+1)
        elif tod[0] == date[0]:
            if tod[1] > date[1]:
                answer.append(idx+1)
            elif tod[1] == date[1]:
                if tod[2] > date[2]:
                    answer.append(idx+1)

    return answer


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
print(solution(terms = ["B 100"],privacies = ["2019.12.1 B"],today = "2020.11.28"))