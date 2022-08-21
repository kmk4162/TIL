-- user에서 가장 나이가 작은 사람의 수는?

select 
count(*) as '인원(명)'
from users
where age = (
select min(age)
from users)
;

-- user에서 계좌 잔고가 평균보다 높은 사람의 수는?
select 
balance,
count(*) as '인원(명)'
from users
where balance > (
select avg(balance)
from users)
;

-- users에서 '유은정'과 같은 지역에 사는 사람의 수는?
SELECT
country,
count(*) as '인원(명)' 
from users
where country = (
select country
from users
where last_name = '유' AND
first_name = '은정');

-- 전체 인원과 평균 연봉, 평균 나이를 출력하고 싶으면?
-- count(*), avg(balance), avg(age)
SELECT
count(*),
avg(balance),
avg(age)
from users;

--특정 성씨에서 가장 어린 사람들의 이름과 나이
select 
last_name as 성,
min(age)
from users
group by last_name;

SELECT
last_name,
first_name,
age
from users
where (last_name, age) in (
select 
last_name as 성,
min(age)
from users
group by last_name)
order by last_name;

SELECT *
FROM invoices
WHERE BillingState ISNULL
ORDER BY InvoiceDate DESC
LIMIT 5;

SELECT
count(*) AS '고객 수',
Country
FROM customers
GROUP BY Country
ORDER BY count(*) DESC
LIMIT 5;

