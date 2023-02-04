'''
규칙에 맞지 않는 아이디 입력 -> 규칙에 맞는 유사한 아이디의 추천

- 3 <= len(user_id) <= 15
- 소문자, -, _, .
    - 단 . 는 연속x, 처음과 끝 x

1. 대문자 -> 소문자
2. 소문자, 숫자, "-, _,." 제외 삭제
3. ".." >  "." 치환
4. 처음과 끝 "." 제거
5. 빈문자열 "a" 추가
6. 15자 이상 -> :16, 마지막이 . 이면 그것도 삭제
7. 2자 이하면 3자 이상이 될때까지 마지막 문자열을 붙임.

'''

def solution(new_id):
    no_s_char = "~!@#$%^&*()=+[{]}:?,<>/"
    new_id = new_id.lower()
    for i in no_s_char:
        new_id = new_id.replace(i, '')
    m = reversed(['.'*j for j in range(2, 16)])
    for s in m:
        new_id = new_id.replace(s, '.')

    new_id = new_id.strip('.')

    if not new_id:
        new_id += 'a'
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id.rstrip('.')
    while len(new_id) <= 2:
        last_s = new_id[-1]
        new_id += last_s
    return new_id





print(solution("...!@BaT#*..y.abcdefghijklm")) #"bat.y.abcdefghi"
print(solution("z-+.^.")) #	"z--"
print(solution("=.=")) #"aaa"
print(solution("123_.def")) #"123_.def"
print(solution("abcdefghijklmn.p")) #"abcdefghijklmn"
