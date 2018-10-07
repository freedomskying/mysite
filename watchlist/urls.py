from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'watchlist'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('service/', views.DowjIdentifyView.as_view(), name='service'),
    path('record_query/', views.record_query, name='record_query'),
    path('record_result/', views.record_result, name='record_result'),
    path('record_detail/<int:record_id>', views.record_detail, name='record_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
