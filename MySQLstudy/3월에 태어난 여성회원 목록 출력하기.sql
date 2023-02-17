-- 생일이 3월 & 여성회원의 id ,이름, 성별, 생년월일 출력
-- 전화번호 NULL 이면 제외
-- 결과는 회원 Id 기준 오름 차순
SELECT
    MEMBER_ID,
    MEMBER_NAME,
    GENDER,
    DATE_FORMAT(DATE_OF_BIRTH,'%Y-%m-%d') AS DATE_OF_BIRTH
    FROM MEMBER_PROFILE
    WHERE SUBSTR(DATE_OF_BIRTH, 6, 2) = '03' && GENDER = 'W' && TLNO != 'NULL'
    ORDER BY MEMBER_ID