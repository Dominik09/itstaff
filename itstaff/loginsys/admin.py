from django.contrib import admin
from .forms import AdminUserChangeForm, AdminUserAddForm
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    form = AdminUserChangeForm
    add_form = AdminUserAddForm
    fieldsets = (
        (None,
            {'fields':(
                'username',
                'password')}),

        ('Personal info',
            {'fields':(
                'first_name',
                'last_name',
                'email',
                'birth_date',
                'gender',
                'is_active',
                'specialization',
                'category',)}),

        ('Important dates',
            {'fields':(
                'last_login',
                'date_joined')})
    )
    add_fieldsets = (
        (None,
            {'classes':('wide',),
            'fields':('username', 'email', 'password1', 'password2')}),
    )

admin.site.register(User, UserAdmin)