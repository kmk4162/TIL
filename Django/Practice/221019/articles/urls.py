from . import views
from django.urls import path

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'), # 데이터 목록 조회
    path('<int:pk>/', views.detail, name='detail'), # 데이터 정보 조회
    path('create/', views.create, name='create'), # 데이터 생성
]