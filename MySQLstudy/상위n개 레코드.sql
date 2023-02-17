-- 동물보호소에서 가장 먼저 들어온 동물의 이름을 조회하는 sql 문을 작성하시오

SELECT
    NAME
    FROM ANIMAL_INS
    ORDER BY DATETIME
    LIMIT 1