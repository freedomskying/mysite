from django.contrib import admin
from .models import Dept, Emp, Bonus, Salgrade

admin.site.register(Dept)
admin.site.register(Emp)
admin.site.register(Bonus)
admin.site.register(Salgrade)

# Register your models here.
