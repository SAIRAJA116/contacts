from django.contrib import admin
from .models import *

# Register your models here.


class UserAdminConfig(admin.ModelAdmin):
    ordering = ("name",)
    list_display = ('email', "name")
    search_fields = ('email', "name")


admin.site.register(NewUser, UserAdminConfig)
admin.site.register(Contact)
