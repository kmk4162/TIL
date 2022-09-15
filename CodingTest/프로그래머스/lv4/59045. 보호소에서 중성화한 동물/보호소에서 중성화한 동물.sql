-- 코드를 입력하세요
# Spayed female 암컷이 중성화
# Neutered Male 수컷이 중성화
# intact male/female 원래 수컷/암컷

SELECT
A.animal_id, A.animal_type, A.name
from animal_ins A inner join animal_outs B
on A.animal_id = B.animal_id
where A.sex_upon_intake != B.sex_upon_outcome
# where (A.sex_upon_intake = 'Intact Male' and B.sex_upon_outcome = 'Neutered Male') or
# (A.sex_upon_intake = 'Intact Female' and B.sex_upon_outcome = 'Spqyed Male')
order by A.animal_id
