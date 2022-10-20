from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'), # 로그인
    path('logout/', views.logout, name='logout'), # 로그아웃
    path('<int:user_pk>/', views.detail, name='detail'), # 회원 정보 조회
]