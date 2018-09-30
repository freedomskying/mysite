from django.contrib import admin

# Register your models here.
from myaccounts.models import UserProfile

admin.site.register(UserProfile)
