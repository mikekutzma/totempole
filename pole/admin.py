from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import User, Change

admin.site.register(Change)

@admin.register(User)
class UserAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name','ranking')
