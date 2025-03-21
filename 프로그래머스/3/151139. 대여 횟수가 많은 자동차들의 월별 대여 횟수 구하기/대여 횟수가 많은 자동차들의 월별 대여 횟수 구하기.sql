SELECT EXTRACT(MONTH FROM START_DATE) AS MONTH,
       CAR_ID,
       COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE CAR_ID IN (SELECT CAR_ID
                 FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                 WHERE EXTRACT(MONTH FROM START_DATE) IN (8, 9, 10)
                 GROUP BY CAR_ID
                 HAVING COUNT(*) >= 5)
AND EXTRACT(MONTH FROM START_DATE) >= 8
AND EXTRACT(MONTH FROM START_DATE) < 11
GROUP BY EXTRACT(MONTH FROM START_DATE), CAR_ID
ORDER BY MONTH, CAR_ID DESC
       