SELECT ID,
       FISH_NAME,
       LENGTH
FROM FISH_INFO A, FISH_NAME_INFO B
WHERE A.FISH_TYPE = B.FISH_TYPE
AND (A.FISH_TYPE, LENGTH) IN (SELECT FISH_TYPE,
                                  MAX(LENGTH)
                                  FROM FISH_INFO
                                  GROUP BY FISH_TYPE)
ORDER BY ID