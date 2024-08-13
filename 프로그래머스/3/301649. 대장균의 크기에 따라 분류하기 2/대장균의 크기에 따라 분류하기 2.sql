SELECT A.ID,
       CASE WHEN A.LEVEL = 1 THEN 'CRITICAL'
            WHEN A.LEVEL = 2 THEN 'HIGH'
            WHEN A.LEVEL = 3 THEN 'MEDIUM'
            ELSE 'LOW'
            END AS COLONY_NAME
FROM (SELECT ID,
             NTILE(4)
                    OVER(ORDER BY SIZE_OF_COLONY DESC) AS LEVEL
                    FROM ECOLI_DATA
                    ) A
ORDER BY A.ID