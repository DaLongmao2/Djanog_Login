from django.urls import path
from Login import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.index2, name='index2'),
    path('register/', views.register, name='register'),
    path('delete/', views.delete, name='delete'),
    path('send_email/', views.send_email, name='send_email'),
    path('test/<token>', views.test, name='test'),
]
