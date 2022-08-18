SELECT is_drinking, AVG(waist), count(*)
FROM healthcare
WHERE is_drinking != ''
GROUP BY is_drinking;

SELECT AVG(age), AVG(height) '평균 키', AVG(weight) '평균 몸무게'
FROM healthcare
GROUP BY age
HAVING AVG(height) >= 160 AND AVG(weight) >= 60;