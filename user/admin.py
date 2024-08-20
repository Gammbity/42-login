from django.contrib import admin
from user import models
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

@admin.register(models.User)
class UserModelAdmin(UserAdmin):
    ordering = ('telegram_id',)
    list_display = ['full_name', 'telegram_id']
    list_display_links =['full_name', 'telegram_id']
    search_fields = ("telegram_id", "full_name")
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        (None, {"fields": ("telegram_id", "password")}),
        (_("Personal info"), {"fields": ("full_name", "phone")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("telegram_id", "password1", "password2"),
            },
        ),
    )