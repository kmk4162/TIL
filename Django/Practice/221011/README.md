# ⚙️회원 가입 서비스 만들기

## 1. 가상환경 및 Django & 사전 설정

### 🧩 가상환경 생성 및 실행

- 가상환경 폴더를 `.gitignore`로 설정을 해둔다.

```
$ python -m venv venv
$ source venv/Scripts/activate
(venv) $
```

<br>

### 🧩 Django 설치 및 기록

```
$ pip install django==3.2.13
$ pip freeze > requirements.txt
```

<br>

### 🧩 Django 프로젝트 생성

```
$ django-admin startproject pjt .
```

<br>

### 🧩 accounts app 생성 및 등록

```
$ pip manage.py startapp accounts
```

```
# settings.py

INSTALLED_APPS = [
	'articles', # 기존 CRUD app
	'accounts', # 새로 추가할 app
]
```

> auth와 관련한 경로나 키워드들을 Django 내부적으로 accounts라는 이름으로 사용하고 있기 때문에 되도록 accounts로 지정하는 것을 권장
>
> 다른 이름으로 설정해도 되지만 나중에 추가 설정을 해야 할 일들이 생기게 됨

<br>

### 🧩 URL 분리 및 mapping

```python
# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
]
```

```python
# pjt/urls.py

urlpatterns = [
    ...
    path('accounts/', include('accounts.urls')),
]
```

<br>

## 2. Model & Form 형성

### 🧩 Model 상속 받기

```python
# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
```

> Django의 AbstractUser를 상속받아서 User 모델을 만든다

<br>

### 🧩 회원가입 Form 만들기

```python
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
```

> 내장 회원가입 폼인 UserCreationForm을 상속받은 CustomUserCreationForm을 사용
>
> User 모델을 사용하기 위해 models.py에서 User를 import 해옴

<br>

## 3. 기능 만들기(View & Template)

### 🧩 회원가입(Create)

http://127.0.0.1:8000/accounts/signup/

CustomUserCreationForm을 활용

```django
{% comment %} index.html {% endcomment %}

{% block body %}
<h1>목록</h1>
{% for user in users %}
<table class="table">
  <thead class="fw-bold">
    <tr>
      <th scope="col">pk</th>
      <th scope="col">username</th>
      <th scope="col">email</th>
    </tr>
  </thead>
  <tbody>
  {% for user in users %}
    <tr>
      <td>{{ user.pk }}</td>
      <td>{{ user.username }}</td>
      <td>{{ user.email }}</td>
    </tr>
  </tbody>
  {% endfor %}
</table>
{% endfor %}
<a href="{% url 'accounts:signup' %}">
  <button type="button" class="btn btn-primary">Sign</button>
</a>
{% endblock body %}
```

```python
# views.py

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:   
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
```

> 기존 방식에서는 model을 직접 정의해서 ModelForm을 상속받은 User로 썼지만, 이제는 UserCreationForm을 상속받은 CustomUserCreationForm을 사용함

![image-20221012010228719](README.assets/image-20221012010228719.png)

<br>

### 🧩 회원 목록 조회(Read)

http://127.0.0.1:8000/accounts/

```python
def index(request):
    users = get_user_model().objects.all()
    context = {
        'users': users
    }
    return render(request, 'accounts/index.html', context)
```

```django
{% block body %}
<h1>목록</h1>
<table class="table">
  <thead class="fw-bold">
    <tr>
      <th scope="col">pk</th>
      <th scope="col">username</th>
      <th scope="col">email</th>
      <th scope="col">detail</th>
    </tr>
  </thead>
  <tbody>
  {% for user in users %}
    <tr>
      <td>{{ user.pk }}</td>
      <td>{{ user.username }}</td>
      <td>{{ user.email }}</td>
      <td><a href="{% url 'accounts:detail' user.pk %}">
        <button type="button" class="btn btn-primary">See Detail</button>
      </a></td>
    </tr>
  </tbody>
  {% endfor %}
</table>
<a href="{% url 'accounts:signup' %}">
  <button type="button" class="btn btn-primary">Sign</button>
</a>
{% endblock body %}
```

> User 참조할 때 get_user_model()를 사용한다

![image-20221012010411200](README.assets/image-20221012010411200.png)

<br>

### 🧩 회원 상세 정보 조회(Read)

 http://127.0.0.1:8000/accounts/<user_pk>/

```
def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user' : user,
    }
    return render(request, 'accounts/detail.html', context)
```

![image-20221012010610158](README.assets/image-20221012010610158.png)
