from django.urls import path, re_path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('', views.IndexView.as_view(), name='index'),
    re_path(r'^category/$', views.CategoryListView.as_view(), name='category_list'),
    re_path(r'^category/(?P<slug>[-\w]+)/$', views.CategoryDetailView.as_view(), name='category_detail'),
]
