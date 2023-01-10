# 로그인 성공

'''
id_pw = [id : 소문자, 숫자, pw : 숫자]
둘다 맞아야 login
아이디 불일치 : fail
아이디 일치, pw 불일치 : wrong pw
'''


def solution(id_pw, db):
    answer = ''
    for db_idx in range(len(db)):
        data = db[db_idx]
        if id_pw[0] == data[0]:
            if id_pw[1] == data[1]:
                return 'login'
            else:
                return 'wrong pw'
    return 'fail'


# test


