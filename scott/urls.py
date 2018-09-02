from django.urls import path
from . import views

app_name = 'scott'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
