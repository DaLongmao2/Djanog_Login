from django.urls import path
from Login import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.index2, name='index2'),
    path('register/', views.register, name='register'),
    path('activate/<token>/<id>', views.activate, name='activate'),
    path('test/', views.test, name='test'),
    path('repeat_input/', views.repeat_input, name='repeat_input'),
    path('reset_pwd/', views.reset_pwd, name='reset_pwd'),
]
