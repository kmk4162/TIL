# 8/19

# 🌇 오전

## 🕓 9:00 ~ 12:00

### ✅ CASE

#### 🟨 CASE 문

- 특정 상황에서 데이터를 변환하여 활용할 수 있음

- ElSE를 생략하는 경우 NULL값이 저장됨

  ```sqlite
  CASE
  	WHEN 조건식 THEN 식
  	WHEN 조건식 THEN 식
  	ELSE 식
  END
  ```

- gender가 1인 경우는 '남자'를, gender가 2인 경우에 '여자'를 출력하고 싶다면?

  ```sqlite
  SELECT 
  id,
  CASE
    WHEN gender = 1 THEN '남자'
    WHEN gender = 2 THEN '여자'
    ELSE '무성'
  END AS 성별
  FROM healthcare
  LIMIT 3;
  ```

  ```
  id  CASE
  --  ----
  1   남자
  2   여자
  3   여자
  ```

  > as를 이용해서 case~  절을 간단하게 표현할 수 있음

- 나이에 따라 청소년(~18), 청년(~30), 중장년(~64)으로 출력하고 싶다면?

  ```sqlite
  select 
  last_name || first_name as 이름,
  age,
  CASE
    when age <= 18 then '청소년'
    when age <= 30 then '청년'
    when age <= 64 then '중장년'
    else '노인'
  END as 분류
  from users
  limit 8;
  ```

  ```
  이름   age  분류
  ---  ---  ---
  유정호  40   중장년
  이경희  36   중장년
  구정자  37   중장년
  장미경  40   중장년
  차영환  30   청년
  이서준  26   청년
  민주원  18   청소년
  김예진  33   중장년
  ```

  > ||를 이용해서 문자열을 합쳐서 표현도 가능

<br>



### ✅ 서브쿼리

#### 🟨 서브쿼리란?

- 특정한 값을 메인 쿼리에 반환하여 활용하는 것

- 실제 테이블에 없는 기준을 이용한 검색이 가능

- 소괄호로 감싸서 사용 가능

- 메인 쿼리는 서브 쿼리의 column을 이용할 수 없음

  ```python
  SELECT *
  FROM 테이블
  WHERE 컬럼1 = (
  	SELECT 컬럼1
  	FROM 테이블
  );
  ```

<br>



#### 🟨 단일행 서브쿼리

- 서브쿼리의 결과가 0 또는 1개인 경우

- 단일행 비교 연산자와 함께 사용

- WHERE 절에서 사용이 가능

- user에서 가장 나이가 작은 사람의 수는?

  ```sqlite
  select
  age,
  count(*) as '인원(명)'
  from users
  where age = (
  select min(age)
  from users)
  ;
  ```

  ```
  age  인원(명)
  ---  -----
  15   39
  ```

  > users에서 제일 작은 나이를 구하고, 그 값 자체를 where 조건절에서 쓰고 싶을때 괄호를 씌워서 사용!

- user에서 계좌 잔고가 평균보다 높은 사람의 수는?

  ```sqlite
  select 
  balance,
  count(*) as '인원(명)'
  from users
  where balance > (
  select avg(balance)
  from users)
  ;
  ```

  ```
  balance  인원(명)
  -------  -----
  250000   222
  ```

- users에서 '유은정'과 같은 지역에 사는 사람의 수는?

  ```sqlite
  SELECT
  country,
  count(*) as '인원(명)' 
  from users
  where country = (
  select country
  from users
  where last_name = '유' AND
  first_name = '은정');
  ```

  ```
  country  인원(명)
  -------  -----
  강원도      101
  ```

<br>



#### 🟨 다중행 서브쿼리

- 서브쿼리 결과가 2개 이상인 경우

- 다중행 비교 연산자와 함께 사용 (IN, EXISTS 등)

- user에서 이은정과 같은 지역에 사는 사람의 수는?

  > 위의 문제와 같다고 생각하지만 이은정은 2명이 존재
  >
  > 따라서 다중행 비교 연산자인 `IN`을 활용해야함!

  ```sqlite
  SELECT
  count(*) as '인원(명)' 
  from users
  where country in (
  select country
  from users
  where last_name = '이' AND
  first_name = '은정');
  ```

  ```
  인원(명)
  -----
  218
  ```

<br> 

#### 🟨 다중컬럼 서브쿼리

- 특정 성씨에서 가장 어린 사람들의 이름과 나이

  ```sqlite
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
  ```

  ```
  last_name  first_name  age
  ---------  ----------  ---
  강          정수          15
  고          우진          15
  고          시우          15
  ...			...			 ...
  황          은정          16
  황          준영          16
  ```

  > 차례대로 나눠서 생각하자
  >
  > 1. users에서 min(age)와 last_name을 각각 구한다음
  > 2. 그 값들을 서브쿼리를 이용해서 활용하는것
  > 3. min(age)와 last_name 쌍은 여러개가 존재하므로 in을 사용해서 출력

<br>




# 🌆 오후

## 🕓 1:00 ~ 6:00

- 
