from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'watchlist'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('service/', views.DowjIdentifyView.as_view(), name='service'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
