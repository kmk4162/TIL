# 8/25

# 🌇 오전

## 🕓 9:00 ~ 12:00

### 🟨 QuerySet API

#### ✅ gt

✔️ Queryseet

```python
Entry.objects.filter(id__gt=4)
```

✔️ SQL Query

```sqlite
SELECT ... WHERE id > 4;
```

<br>

#### ✅ gte

✔️ Queryseet

```python
Entry.objects.filter(id__gte=4)
```

✔️ SQL Query

```sqlite
SELECT ... WHERE id >= 4;
```

<br>

#### ✅ lt, lte

✔️ Queryseet

```python
Entry.objects.filter(id__lt=4)
Entry.objects.filter(id__lte=4)
```

✔️ SQL Query

```sqlite
SELECT ... WHERE id < 4;
SELECT ... WHERE id <= 4;
```

<br>

#### ✅ in

✔️ Queryseet

```python
Entry.objects.filter(id__in = [1, 3, 4])
Entry.objects.filter(headline__in = 'abc')
```

✔️ SQL Query

```sqlite
SELECT ... WHERE id IN [1, 3, 4];
SELECT ... WHERE headline IN ('a', 'b', 'c');
```

<br>

#### ✅ startswith

✔️ Queryseet

```python
Entry.objects.filter(headline__startswith = 'Lennon')
```

✔️ SQL Query

```sqlite
SELECT ... WHERE headline LIKE 'Lennon%';
```

<br>

#### ✅ istartswith ; 대소문자 구별 x

✔️ Queryseet

```python
Entry.objects.filter(headline__istartswith = 'Lennon')
```

✔️ SQL Query

```sqlite
SELECT ... WHERE headline ILIKE 'Lennon%';
```

<br>

#### ✅ endswith

✔️ Queryseet

```python
Entry.objects.filter(headline__endswith = 'Lennon')
Entry.objects.filter(headline__iendswith = 'Lennon')
```

✔️ SQL Query

```sqlite
SELECT ... WHERE headline LIKE '%Lennon';
SELECT ... WHERE headline ILIKE '%Lennon';
```

<br>

#### ✅ contains ; 포함

✔️ Queryseet

```python
Entry.objects.get(headline__contains = 'Lennon')
Entry.objects.get(headline__icontains = 'Lennon')
```

✔️ SQL Query

```sqlite
SELECT ... WHERE headline LIKE '%Lennon%';
SELECT ... WHERE headline ILIKE '%Lennon%';
```

<br>

#### ✅ range

✔️ Queryseet

```python
import datetime
start_date = datetime.date(2005, 1, 1)
end_date = datetime.date(2005, 3, 31)
Entry.objects.filter(pub_date__range=(start_date, end_date))
```

✔️ SQL Query

```sqlite
SELECT ... WHERE pub_date
BETWEEN '2005-01-01' and '2005-03-31';
```

<br>

#### ✅ 복합 활용

✔️ Queryseet

```python
inner_qs = Blog.objects.filter(name__contains='Cheddar')
entries = Entry.objects.filter(blog__in=inner_qs)
```

✔️ SQL Query

```sqlite
SELECT ... WHERE blog.id IN (SELECT id FROM ... WHERE NAME LIKE '%Cheddar%');
```

<br>

#### ✅ 활용

✔️ Queryseet

```python
Entry.objects.all()[0]
```

✔️ SQL Query

```sqlite
SELECT ... LIMIT 1;
```

<br>

#### ✅ 오름차순 정렬

✔️ Queryseet

```python
Entry.objects.order_by('id')
```

✔️ SQL Query

```sqlite
SELECT ... ORDER BY id;
```

<br>

#### ✅ 내림차순 정렬

✔️ Queryseet

```python
Entry.objects.order_by('-id')
```

✔️ SQL Query

```sqlite
SELECT ... ORDER BY id DESC;
```

<br>

### 🟨 ORM 확장 (1:N)

#### ✅ 모델링(ORM)

```python
class Genre(models.Model):
	name = models.CharField(max_length=30)
class Artist(models.Model):
	name = models.CharField(max_length=30)
	debut = models.DateField()
class Album(models.Model):
	name = models.CharField(max_length=30)
	genre = models.ForeignKey('Genre',
on_delete=models.CASCADE)
	artist = models.ForeignKey('Artist',
on_delete=models.CASCADE)
```

> name, genre라고 이름지어야 `name_id`, `genre_id`로 됨!

<br>

#### ✅ models.ForeignKey 필드

- 2개의 필수 위치 인자
  - Model class : 참조하는 모델
  - on_delete : 외래 키가 참조하는 객체가 삭제되었을 때 처리 방식
    - CASCADE : 댓글을 지워야한다
    - PROTECT : 댓글 있으면 글 지우지 못하기
    - SET_NULL : NULL 설정
    - SET_DEFAULT : 기본 값 설정

<br>

#### ✅ Create

```python
artist = Artist.objects.get(id=1)
genre = Genre.objects.get(id=1)

album = Album() 
album.name = '앨범1'
album.artist = artist # 1. 객체의 저장
album.genre = genre
album.save()
```

<br>

#### ✅ 참조 & 역참조

```python
# N => 1 (참조)
# 앨범의 id가 1인 것의
album = Album.objects.get(id=1) # 앨범 객체
# 장르의 이름은..?
album.genre # 장르 객체
# <Genre: Genre object (1)>
album.genre.name
# '발라드'


# 1 => N (역참조)
# 클래스이름_set
# id가 1인 장르의 모든 앨범은?
g1 = Genre.objects.get(id=1)
g1.album_set.all() 
# <QuerySet [<Album: Album object (1)>, <Album: Album object (2)>]>
```

<br>

# 🌆 오후

## 🕓 1:00 ~ 6:00

### 🟨 ORM 실습

#### ✅ 실습 환경 설정

👉 [참고자료](./Practice/220825/README.md)

<br>

#### ✅ 실습08

👉 [실습파일](./Practice/220825/%EC%8B%A4%EC%8A%B508.md)
