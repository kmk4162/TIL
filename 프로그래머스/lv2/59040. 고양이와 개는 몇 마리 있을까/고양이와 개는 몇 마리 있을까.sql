-- 코드를 입력하세요
SELECT
animal_type as 'ANIMAL_TYPE',
count(*) as 'count'
from animal_ins
group by animal_type
order by animal_type
