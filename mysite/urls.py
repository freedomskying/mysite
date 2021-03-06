"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
                  path('polls/', include('polls.urls')),
                  path('article/', include('article.urls')),
                  path('admin/', admin.site.urls),
                  url(r'^', include(router.urls)),
                  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  path('restapp/', include('restapp.urls')),
                  path('watchlist/', include('watchlist.urls')),
                  path('accounts/', include('allauth.urls')),  # allauth
                  url(r'^myrestaurants/', include('myrestaurants.urls')),  # myrestaurants
                  path('smartdoc/', include('smartdoc.urls')),  # smartdoc
                  path('portal/', include('portal.urls')),  # portal
                  # url(r'^silk/', include('silk.urls', namespace='silk')),  # silk
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

LOGIN_REDIRECT_URL = '/accounts/profile/'
