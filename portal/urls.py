from django.urls import path, re_path
from . import views

app_name = 'portal'

urlpatterns = [
    path('', views.portal, name='protal'),
    path('test/', views.test, name='test'),
    path('login/', views.login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^portal/(?P<pk>\d+)/profile/$', views.profile, name='profile'),
    re_path(r'^portal/(?P<pk>\d+)/profile/update/$', views.profile_update, name='profile_update'),
    re_path(r'^portal/(?P<pk>\d+)/pwdchange/$', views.pwd_change, name='pwd_change'),
    re_path(r'^logout/$', views.logout, name='logout'),
]
