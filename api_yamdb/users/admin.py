from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Настройки раздела пользователей."""

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['is_active'].help_text = "Статус пользователя"
        form.base_fields['is_superuser'].help_text = "СуперЮзер"
        return form

    list_display = (
        'username',
        'is_staff',
        'date_joined',
        'role'
    )
    search_fields = ('username', 'role')
    list_editable = ('role', 'is_staff',)
    empty_value_display = '-empty-'
    ordering = ['-date_joined']
    fieldsets = (
        ('Персональные данные',
         {'fields': ('username', 'email', 'date_joined',)}),
        ('Административные права',
         {'fields': ('is_active', 'role', 'is_superuser',)}),
        ('Прочее', {'fields': ('bio', 'password')}),
    )
