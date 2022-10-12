from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'), # 회원 목록 조회
    path('signup/', views.signup, name='signup'), # 회원 가입
    path('<int:pk>/', views.detail, name='detail'), # 각 회원의 정보 조회
    path('login/', views.login, name='login'), # 로그인 기능
    path('logout/', views.logout, name='logout'), # 로그아웃 기능
]