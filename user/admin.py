from django.contrib import admin
from user import models
from django.utils.translation import gettext_lazy as _

@admin.register(models.User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'telegram_id']
    list_display_links = ['full_name']