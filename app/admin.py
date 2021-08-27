from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import Todo, User


class MyUserAdmin(UserAdmin):
    list_display = ['username', 'is_active', 'is_staff', 'is_superuser', ]


class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'status', 'priority', 'close_datetime', ]


admin.site.register(User, MyUserAdmin)
admin.site.register(Todo, TodoAdmin)
