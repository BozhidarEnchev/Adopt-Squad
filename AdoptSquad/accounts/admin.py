from django.contrib import admin
from django.contrib.auth import get_user_model

UserModel = get_user_model()


@admin.register(UserModel)
class AdminAppUser(admin.ModelAdmin):
    list_display = ['username', 'email']
    exclude = ['password']
    ordering = ['-username', '-email']
    fieldsets = [
        (
            'Personal information',
            {'fields': ('username', 'email', 'first_name', 'last_name',)},
        ),
        (
          'Other info',
          {'fields': ('is_active', 'last_login', 'date_joined', 'profile_picture',)}
        ),
        ('Authorization',

            {
                'classes': ('collapse',),
                'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions',),
             }
         )
    ]