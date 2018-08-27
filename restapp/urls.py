from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'restapp'

urlpatterns = [
    url('', views.snippet_list),
    url('/<int:pk>/', views.snippet_detail),
]
