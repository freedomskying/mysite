from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'watchlist'

urlpatterns = [
    # 对外服务
    path('service', views.DowjIdentifyView.as_view(), name='service'),

    # 个人客户查询
    path('record_query/', views.record_query, name='record_query'),
    path('record_result/', views.record_result, name='record_result'),
    path('record_detail/<int:record_id>', views.record_detail, name='record_detail'),

    # 公司客户查询
    path('corp_query/', views.corp_query, name='corp_query'),
    path('corp_result/', views.corp_result, name='corp_result'),
    path('corp_detail/<int:record_id>', views.corp_detail, name='corp_detail'),

    # 公司关系网
    path('corp_associate/', views.corp_associate, name='corp_associate'),
    path('corp_associate_query/', views.corp_associate_query, name='corp_associate_query'),

    # 审计日志
    path('audit_log_query/', views.audit_log_query, name='audit_log_query'),
    path('audit_log_result/', views.audit_log_result, name='audit_log_result'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
