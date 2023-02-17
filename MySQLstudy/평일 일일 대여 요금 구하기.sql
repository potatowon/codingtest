-- 자동차 종류가 suv 인 자동차들의 일일 평균 대여 요금을 출력하는 sql 문 작성하기
-- 소수 첫 번째 자리에서 반올림
-- 컬럼명은 AVERAGE_FEE

SELECT
    ROUND(AVG(DAILY_FEE)) AS AVERAGE_FEE
    FROM CAR_RENTAL_COMPANY_CAR
    WHERE CAR_TYPE = 'SUV';