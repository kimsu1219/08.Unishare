from django.urls import path, include
from . import views

app_name = 'univs'
urlpatterns = [
    path('', views.index, name='index'),
    path('userinfo/<str:roominfo>?<str:roomtime>/', views.userInfo, name='userInfo'),
    path('getpassword/', views.getPassword, name='getPassword'),
]
