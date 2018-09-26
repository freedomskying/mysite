
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'restapp'

# urlpatterns = [
#     url(r'^restapp/$', views.snippet_list),
#     url(r'^restapp/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]

urlpatterns = [
    path('', views.SnippetList.as_view()),
    path('<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
