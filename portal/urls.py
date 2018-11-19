from django.urls import path, re_path
from . import views

app_name = 'portal'

urlpatterns = [
    path('', views.portal, name='protal'),
    path('login/', views.login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    re_path(r'^logout/$', views.logout, name='logout'),
]
