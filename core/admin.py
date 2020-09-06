from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
# models
from core.models import User, Device

# re define user admin
class UserAdmin(BaseUserAdmin):

    # sort
    ordering = ['id']

    # display
    list_display = ['email','name']
    fieldsets = (
        # ラベルなし
        (None, {'fields': ('email', 'password')}),
        # ラベルあり
        (
            _('個人情報'),
            {'fields': ('name',)}
        ),
        (
            _('パーミッション'),
            {'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            )}
        ),
        (
            _('履歴'),
            {'fields': ('last_login',)}
        ),
    )
    # from 'USERを追加'
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','password1','password2')
        }),
    )

# add models on admin pannel
admin.site.register(User, UserAdmin)
admin.site.register(Device)


