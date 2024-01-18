from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = (
        'username',
        'email',
        'is_active',
        'is_staff',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'username',
        'email'
    )
